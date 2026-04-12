# Core Modules - eLoyalty 2.0

## 🎯 Objetivo

Definir los módulos funcionales del **core del producto eLoyalty**, identificando:

- Qué hace cada módulo
- Qué es obligatorio vs opcional
- Qué partes son configurables (multi-marca)
- Qué partes pertenecen estrictamente al core

Este documento es clave para:

- Evitar reinventar la app por cliente
- Identificar oportunidades de configuración
- Acelerar implementación de nuevas marcas

---

## 🧱 Principios

- Todos los módulos aquí descritos pertenecen al **core reusable**
- Ningún módulo debe romper el flujo principal:
  - Vincular tarjeta → Acumular → Redimir
- La personalización debe resolverse vía configuración, no desarrollo

---

## 📦 Lista de Módulos

---

### 1. Splash

**Tipo:** Obligatorio  
**Descripción:**
Pantalla inicial de carga de la app.

**Responsabilidad:**

- Mostrar branding inicial
- Cargar configuración de la marca

**Configurable:**

- Logo
- Colores (background)
- Imagen o animación

---

### 2. Vinculación / Login

**Tipo:** Obligatorio  
**Descripción:**
Permite al usuario vincular su tarjeta de lealtad con el dispositivo.

**Flujo observado en app:**

- Input tarjeta (16 dígitos)
- Nombre completo
- Email
- Teléfono (10 dígitos)

**Notas importantes:**

- No siempre existe "login tradicional"
- Es un modelo de **vinculación de identidad + tarjeta**

**Configurable:**

- Textos
- Placeholder inputs
- Logo
- Fondo
- Activar/desactivar opción de registro

---

### 3. Registro

**Tipo:** Opcional  
**Descripción:**
Alta de usuario cuando no cuenta con tarjeta.

**Flujo:**

- Nombre
- Apellidos
- Estación de servicio
- Teléfono
- Email

**Notas:**

- En muchos clientes NO se usa (flujo físico con tarjeta)
- Debe poder desactivarse completamente

**Configurable:**

- Mostrar / ocultar módulo
- Campos requeridos
- Textos
- Branding visual

---

### 4. Home

**Tipo:** Obligatorio  
**Descripción:**
Pantalla principal del usuario.

**Responsabilidad:**

- Mostrar:
  - Nombre del usuario
  - Tarjeta vinculada
  - Saldo de puntos
- Navegación a funcionalidades principales

**Entradas visuales observadas:**

- Tarjeta (componente clave)
- Cards de navegación (tiles con imagen)

**Navegación:**

- Estaciones de servicio
- Tiendas participantes
- Acumular puntos
- Redimir puntos
- Promociones / premios

**Configurable:**

- Orden de módulos
- Imágenes de banners
- Acciones visibles
- Colores y estilos
- Textos

---

### 5. Estaciones de Servicio

**Tipo:** Obligatorio  
**Descripción:**
Listado de estaciones del grupo gasolinero.

**Funcionalidades:**

- Búsqueda (nombre / dirección)
- Lista de estaciones
- Acciones:
  - Ver web
  - Llamar
  - Abrir mapa

**Configurable:**

- Estilo de cards
- Iconos
- Colores
- Información visible

---

### 6. Acumular Puntos (Scan)

**Tipo:** Obligatorio (CORE CRÍTICO)  
**Descripción:**
Permite escanear ticket ATIO para acumular puntos.

**Flujo:**

1. Seleccionar estación
2. Seleccionar tipo de combustible
3. Escanear código del ticket

**Dependencias:**

- Integración con ATIO
- Lectura de código (QR / código de barras)

**Notas:**

- Es el módulo más importante del negocio
- No debe ser modificado por marca (solo apariencia)

**Configurable:**

- Header
- Colores
- Textos

---

### 7. Redimir Puntos

**Tipo:** Obligatorio  
**Descripción:**
Permite canjear puntos por productos o beneficios.

**Flujo:**

1. Seleccionar premio
2. Seleccionar estación
3. Confirmar redención

**Datos mostrados:**

- Puntos acumulados
- Puntos requeridos
- Puntos restantes

**Configurable:**

- Catálogo (backend)
- UI visual
- Textos
- Colores

---

### 8. Perfil

**Tipo:** Obligatorio  
**Descripción:**
Información del usuario vinculado.

**Datos mostrados:**

- Número de tarjeta
- Nombre
- Email
- Teléfono

**Acciones:**

- Desvincular cuenta (logout)
- Eliminar cuenta

**Configurable:**

- Campos visibles
- Textos
- Estilo visual

---

### 9. Notificaciones

**Tipo:** Obligatorio  
**Descripción:**
Centro de notificaciones del usuario.

**Contenido:**

- Promociones
- Avisos
- Mensajes del sistema

**Dependencias:**

- Firebase / Push notifications

**Configurable:**

- Tipos de notificación
- Copy
- Orden

---

### 10. Mis Redenciones

**Tipo:** Obligatorio  
**Descripción:**
Historial de redenciones del usuario.

**Contenido:**

- Lista de premios redimidos
- Códigos generados
- Estado de redención

**Notas observadas:**

- Estado vacío manejado ("No tienes redenciones")

**Configurable:**

- Textos empty state
- UI

---

### 11. Contenido Legal

**Tipo:** Obligatorio  
**Descripción:**
Pantallas legales accesibles desde menú lateral.

**Incluye:**

- Términos y Condiciones
- Política de Privacidad

**Configurable:**

- Contenido legal (por cliente)
- Títulos
- Formato

---

### 12. Navegación

**Tipo:** Obligatorio  
**Descripción:**
Estructura de navegación global.

**Componentes:**

- Bottom tab bar
- Menú lateral (drawer)
- Header con:
  - Logo
  - Notificaciones
  - Back

**Configurable:**

- Íconos
- Orden
- Secciones visibles
- Estilo visual

---

## 🧠 Observaciones Clave para Escalabilidad

### 1. El verdadero core ya está bien definido

No necesitas rediseñar funcionalidad, necesitas:

→ **estandarizar + parametrizar**

---

### 2. El Home es un "layout dinámico"

Debe evolucionar a:

```json
{
  "home_modules": [
    "card_balance",
    "stations",
    "scan",
    "redeem",
    "promotions"
  ]
}
```

