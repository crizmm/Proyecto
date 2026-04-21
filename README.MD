# 🌍 EcoBot – Sistema de Retos Ambientales en Discord

---

## 🧠 Descripción del proyecto

EcoBot es un bot de Discord diseñado para fomentar hábitos sostenibles a través de retos ambientales interactivos. Los usuarios pueden recibir desafíos ecológicos, completarlos y ganar puntos, lo que les permite avanzar en un sistema de roles dentro del servidor.

El objetivo principal es **concientizar sobre el cuidado del medio ambiente** de forma divertiday simple.

---

## 🎯 Finalidad y usos

Este proyecto puede utilizarse para:

* Promover hábitos ecológicos en comunidades online
* Educar sobre el impacto ambiental cotidiano
* Gamificar el aprendizaje ambiental
* Crear dinámicas de participación en servidores de Discord

---

## ⚙️ Funciones y características

### 🌱 Sistema de retos

* Asignación aleatoria de retos ambientales
* Cada reto tiene:

  * Descripción
  * Dificultad
  * Recompensa en puntos
  * Un ID

### ✅ Sistema de progreso

* Los usuarios pueden marcar retos como completados
* Se guarda el estado en una base de datos

### 💰 Sistema de puntos

* Cada reto completado otorga puntos
* Los puntos se acumulan por usuario

### 🏆 Sistema de roles automático

* Los usuarios obtienen roles según su puntuación:

  * 🌱 Eco Novato
  * ♻️ Eco Comprometido
  * 🌿 Eco Líder
  * 🌍 Héroe Verde

### 📊 Base de datos (SQLAlchemy)

* Manejo de datos con SQLite
* Tablas:

  * `usuarios`
  * `retos`

### 🌍 Extras

* Comando de datos ambientales aleatorios
* Calculadora básica de huella de carbono

---

## 🖥️ Demostración

Ejemplo de uso:

```
!asignar_retos
→ Te da un reto con ID

!completar luces
→ Marca el reto como completado y da puntos

!progreso
→ Muestra tus retos activos
```


---

## 🛠️ Instalación y uso

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/eco-bot.git
cd eco-bot
```

### 2. Instalar dependencias

```
pip install discord.py sqlalchemy
```

### 3. Configurar el bot

* Crea un bot en Discord Developer Portal
* Copia tu token
* Sustitúyelo en:

```python
bot.run("TU_TOKEN_AQUI")
```

### 4. Ejecutar

```
python main.py
```

---

## 💬 Comentarios y contribuciones

Puedes mejorar este proyecto:

* Reportando errores
* Sugiriendo nuevos retos
* Mejorando el sistema de ranking (próximamente 👀)
* Haciendo fork del repositorio

---

## 🏁 Conclusión

EcoBot demuestra cómo la programación puede utilizarse para generar impacto positivo en la sociedad. Al combinar tecnología, educación y gamificación, este proyecto busca motivar a las personas a adoptar hábitos más sostenibles de manera divertida.

Este es solo el comienzo — futuras mejoras incluyen:

* 🏆 Sistema de ranking global
* 📈 Estadísticas avanzadas
* 🎮 Interfaz más interactiva

---

🌍 *Pequeñas acciones, grandes cambios.*
