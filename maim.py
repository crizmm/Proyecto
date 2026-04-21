import discord
import random
from discord.ext import commands
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine("sqlite:///retos.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


class Reto(Base):
    __tablename__ = "retos"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    reto_id = Column(String)
    reto_nombre = Column(String)
    descripcion = Column(String)
    dificultad = Column(Integer)
    recompensa = Column(Integer)
    completado = Column(Integer)


class Usuario(Base):
    __tablename__ = "usuarios"

    user_id = Column(String, primary_key=True)
    nombre_usuario = Column(String)
    puntuacion = Column(Integer, default=0)


Base.metadata.create_all(engine)


@bot.event
async def on_ready():
    print(f'✅ Ha iniciado sesión como {bot.user}')


@bot.command()
async def menu(ctx):
    menu = (
        "🌍 **Menú Principal** 🌍\n"
        "1️⃣ !changefacts - Dato ambiental\n"
        "2️⃣ !footprint - Calcular tu huella de carbono (aprox.)\n"
        "3️⃣ !asignar_retos - Obtener un nuevo reto ambiental\n"
        "4️⃣ !progreso - Ver tu progreso en los retos\n"
        "5️⃣ !completar <ID del reto> - Marcar un reto como completado\n"
        "6️⃣ !roles - Ver tus roles y niveles de compromiso ambiental\n"
    )
    await ctx.send(menu)


@bot.command()
async def changefacts(ctx):
    facts = [
        ("🌡️ La temperatura global ha aumentado "
         "aproximadamente 1.2°C desde la era"
         " preindustrial."),
        ("🌊 El nivel del mar ha subido alrededor de 20 cm "
         "en el último siglo."),
        ("🔥 Los eventos climáticos extremos, como incendios "
         "forestales y huracanes, se han vuelto más "
         "frecuentes e intensos."),
        ("❄️ El hielo marino del Ártico ha disminuido en un "
         "40% desde 1979."),
        ("🌍 La deforestación contribuye a aproximadamente "
         "el 10% de las emisiones de CO₂."),
        ("⚡ La producción de energía renovable ha aumentado "
         "un 20% en la última década."),
        ("🚗 El transporte es responsable de aproximadamente "
         "el 14% de las emisiones globales.")
    ]
    fact = random.choice(facts)
    await ctx.send(fact)


@bot.command()
async def footprint(ctx):
    huella = 0

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    # 🚗 Transporte
    await ctx.send(
        "🚗 ¿Cuántos km viajas en coche por semana? "
        "(solo número)"
    )
    msg = await bot.wait_for("message", check=check)
    km = int(msg.content)
    huella += km * 52 * 0.2

    # ⚡ Energía
    await ctx.send(
        "⚡ ¿Usas aire acondicionado o calefacción? (si/no)"
    )
    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() in ["si", "sí"]:
        huella += 1500
    else:
        huella += 800

    # 🍔 Alimentación
    await ctx.send(
        "🍔 ¿Con qué frecuencia comes carne? "
        "(nunca / a veces / diario)"
    )
    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() == "diario":
        huella += 1500
    elif msg.content.lower() == "a veces":
        huella += 800
    else:
        huella += 300

    # 🛍️ Consumo
    await ctx.send(
        "🛍️ ¿Compras ropa frecuentemente? (si/no)"
    )
    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() in ["si", "sí"]:
        huella += 600
    else:
        huella += 200

    # 📊 Resultado final
    if huella < 4000:
        nivel = "🌱 Bajo"
    elif huella < 8000:
        nivel = "⚖️ Medio"
    else:
        nivel = "🔥 Alto"

    await ctx.send(
        f"🌍 Tu huella estimada es **{int(huella)} kg CO₂/año**\n"
        f"Nivel: {nivel}"
    )


@bot.command()
async def asignar_reto(ctx):
    retos = {
        "caminata": {
            "nombre": "🚶‍♂️ Caminata y bicicleta en trayectos cortos",
            "descripcion": (
                "🚶‍♂️ Camina o usa bicicleta para trayectos cortos."
            ),
            "dificultad": 3,
            "recompensa": 500
        },
        "luces": {
            "nombre": "💡 Apagar luces innecesarias",
            "descripcion": (
                "💡 Apaga las luces cuando no las necesites."
            ),
            "dificultad": 2,
            "recompensa": 300
        },
        "reciclaje": {
            "nombre": "♻️ Reciclaje activo",
            "descripcion": (
                "♻️ Separa tus residuos y recíclalos."
            ),
            "dificultad": 4,
            "recompensa": 400
        },
        "carne": {
            "nombre": "🍽️ Reducción de carne",
            "descripcion": (
                "🍽️ Reduce tu consumo de carne a la mitad."
            ),
            "dificultad": 5,
            "recompensa": 600
        },
        "ducha": {
            "nombre": "🚿 Ducha eficiente",
            "descripcion": (
                "🚿 Reduce tu tiempo de ducha a 5 minutos."
            ),
            "dificultad": 3,
            "recompensa": 400
        },
        "agua": {
            "nombre": "💧 Uso responsable del agua",
            "descripcion": (
                "💧 Cierra el grifo mientras te cepillas los dientes."
            ),
            "dificultad": 2,
            "recompensa": 200
        }
    }

    reto_id = random.choice(list(retos.keys()))
    data = retos[reto_id]
    msg = (
        f"¡Nuevo Reto asignado! 🌟 Tu reto ambiental es: "
        f"{data['nombre']}\nDescripción: {data['descripcion']}\n"
        f"ID del reto: `{reto_id}`\nDificultad: {data['dificultad']} | "
        f"Recompensa: {data['recompensa']} puntos"
        "Para completar el reto, usa el comando: `!completar <ID del reto>`"
    )
    await ctx.send(msg)

    nuevo_reto = Reto(
        user_id=str(ctx.author.id),
        reto_id=reto_id,
        reto_nombre=data["nombre"],
        descripcion=data["descripcion"],
        dificultad=data["dificultad"],
        recompensa=data["recompensa"],
        completado=0
    )

    session.add(nuevo_reto)
    session.commit()


@bot.command()
async def progreso(ctx):
    user_id = str(ctx.author.id)
    retos_usuario = session.query(Reto).filter_by(user_id=user_id).all()

    if not retos_usuario:
        await ctx.send("❌ No tienes retos asignados.")
        return

    mensaje = "📊 **Tu Progreso en Retos** 📊\n"
    for reto in retos_usuario:
        estado = "✅ Completado" if reto.completado else "❌ Pendiente"
        mensaje += f"- {reto.reto_nombre}: {estado}\n"

    await ctx.send(mensaje)


@bot.command()
async def completar(ctx, reto_id):
    user_id = str(ctx.author.id)

    reto = session.query(Reto).filter_by(
        user_id=user_id,
        reto_id=reto_id
    ).first()

    if not reto:
        await ctx.send("❌ Reto no encontrado")
        return

    reto.completado = 1
    recompensa = reto.recompensa

    usuario = session.query(Usuario).filter_by(
        user_id=user_id
    ).first()

    if not usuario:
        usuario = Usuario(
            user_id=user_id,
            nombre_usuario=str(ctx.author),
            puntuacion=0
        )
        session.add(usuario)

    usuario.puntuacion += recompensa
    puntos = usuario.puntuacion

    session.commit()

    # 🎯 VERIFICAR ROL

    member = ctx.guild.get_member(ctx.author.id)
    role_eco_novato = 123456789012345678
    role_novato = ctx.guild.get_role(role_eco_novato)

    role_eco_comprometido = 1491928266389455038
    role_comprometido = ctx.guild.get_role(role_eco_comprometido)

    role_eco_lider = 1491928606178414622
    role_lider = ctx.guild.get_role(role_eco_lider)

    role_heroe_verde = 1491928668811825162
    role_heroe = ctx.guild.get_role(role_heroe_verde)

    PUNTOS_NOVATO = 500
    PUNTOS_COMPROMETIDO = 1000
    PUNTOS_LIDER = 2000
    PUNTOS_HEROE = 4000

    if puntos >= PUNTOS_HEROE:
        if role_heroe and role_heroe not in member.roles:
            await member.add_roles(role_heroe)
            await ctx.send("🌍 ¡Eres un Héroe Verde!")

    elif puntos >= PUNTOS_LIDER:
        if role_lider and role_lider not in member.roles:
            await member.add_roles(role_lider)
            await ctx.send("🌿 ¡Ahora eres Eco Líder!")

    elif puntos >= PUNTOS_COMPROMETIDO:
        if role_comprometido and role_comprometido not in member.roles:
            await member.add_roles(role_comprometido)
            await ctx.send("♻️ ¡Eres Eco Comprometido!")

    elif puntos >= PUNTOS_NOVATO:
        if role_novato and role_novato not in member.roles:
            await member.add_roles(role_novato)
            await ctx.send("🌱 ¡Eres Eco Novato!")

    # Mensaje final
    await ctx.send(
        f"✅ Reto completado. Ganaste {recompensa} puntos.\n💰 Total: {puntos}"
    )


@bot.command()
async def roles(ctx):
    await ctx.send(
        "Los roles que hay son:\n- 🌍 Héroe Verde\n- 🌿 Eco Líder\n"
        "- ♻️ Eco Comprometido\n- 🌱 Eco Novato"
    )
bot.run(
    ""
    "-f_U9rQ"
)
