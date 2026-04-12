# Business Context

## Current Sales Model

El producto actualmente se comercializa a grupos gasolineros que ya cuentan con infraestructura tecnológica provista por ATIO.

La estrategia de venta se apoya en esta integración existente, facilitando la adopción del sistema de lealtad dentro del ecosistema operativo de las estaciones de servicio.

---

## Implementation Model

Cada nueva marca requiere una adaptación de la aplicación móvil (Android e iOS), la cual actualmente se maneja mediante repositorios separados con una personalización básica por cliente.

---

## Implementation Time

El tiempo promedio para adaptar la aplicación a una nueva marca es de aproximadamente 3 días, distribuidos de la siguiente manera:

- 1 día: diseño y adaptación de assets (logos, imágenes, elementos gráficos)
- 1 día: implementación en Android (cambio de imágenes, configuración, build y publicación)
- 1 día: implementación en iOS (mismo proceso que Android)

Este proceso incluye también la preparación y publicación en las tiendas (App Store y Google Play).

---

## Recurrent Changes per Client

Los elementos que cambian en cada implementación incluyen:

- Paleta de colores
- Headers
- Imágenes principales (aproximadamente 12 assets)
- Logos
- Iconos de aplicación
- Términos y condiciones
- Políticas de privacidad
- Archivos de configuración (ej. GoogleService-Info)

---

## Stable Core Features

Las funcionalidades principales del producto se mantienen estables entre clientes:

- Splash screen
- Registro de usuario
- Login
- Notificaciones
- Acumulación de puntos
- Canje/redención de recompensas
- Visualización de estaciones
- Pantalla principal (home)

Esto indica que el producto ya cuenta con un core funcional bien definido y reutilizable.

---

## Operational Bottlenecks

Los principales puntos de fricción en el proceso actual son:

- Preparación de assets gráficos (especialmente sin apoyo de diseño)
- Ajuste manual de imágenes a múltiples tamaños
- Limpieza y adaptación de logos proporcionados por el cliente
- Proceso de build y publicación en tiendas
- Manejo separado de Android e iOS

Estos factores generan una carga operativa significativa que no está directamente relacionada con el valor del producto.

---

## Client Profile

Los clientes actuales son:

- Grupos gasolineros
- Operadores con múltiples estaciones de servicio

---

## Customization Requests

Algunos clientes solicitan cambios que rompen el flujo estándar de implementación:

- Modificaciones en la pantalla principal (home)
- Ajustes visuales más allá de branding básico
- Nuevas funcionalidades específicas para su marca

Estas solicitudes introducen variabilidad en el producto y aumentan el esfuerzo de implementación.

---

## Key Observations

- El core del producto es estable y reutilizable
- La mayor parte del tiempo de implementación se consume en tareas operativas
- Existe una oportunidad clara de:
  - Estandarizar personalización
  - Automatizar generación de assets
  - Reducir fricción en builds y publicación
  - Separar configuración de desarrollo

---

## Strategic Implications

Para evolucionar el producto hacia un modelo más escalable, es necesario:

- Reducir la dependencia de cambios manuales por cliente
- Definir claramente qué es configurable vs custom
- Optimizar el proceso de branding por marca
- Diseñar un sistema que permita generar versiones por cliente de forma más rápida y controlada

