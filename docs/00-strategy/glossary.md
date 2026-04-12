# Glosario (00-strategy)

Términos recurrentes en la estrategia del producto. Las definiciones resumen el uso en estos documentos, no un diccionario técnico genérico.

## Negocio y mercado

- **Grupo gasolinero**: Organización que opera una o varias estaciones de servicio; cliente principal del producto.
- **Estación de servicio / sucursal**: Punto de venta donde el consumidor compra combustible u otros productos y donde opera el programa de lealtad.
- **ATIO**: Proveedor tecnológico del ecosistema de cobro y operación; la venta y la integración suelen apoyarse en clientes que ya usan su infraestructura.
- **Mercado objetivo (México)**: ~350 grupos gasolineros; buena parte con tecnología compatible (p. ej. ATIO), mercado acotado pero definido.

## Producto y propuesta de valor

- **Plataforma de lealtad**: Sistema de fidelización para estaciones de servicio, integrado al flujo de compra (p. ej. QR en ticket → puntos → recompensas).
- **Programa de lealtad**: Conjunto de reglas e instrumentos (app, puntos, canjes) para retener e incentivar recompra.
- **Integración operativa**: Encaje con POS, hardware especializado y ecosistema del grupo; principal diferenciador frente a soluciones genéricas.
- **White-label / SaaS (visión)**: Modelo futuro deseado: implementaciones rápidas, personalización controlada y menor esfuerzo por cliente.

## Usuarios y compra

- **Usuario final / consumidor**: Persona que escanea el QR, acumula y canjea puntos en la app.
- **Stakeholders del cliente**: Dueños/directores (ROI), marketing (retención), IT (integración); el mensaje debe cubrir negocio y técnica.
- **Ideal Customer Profile (ICP)**: Grupo con infraestructura establecida (p. ej. ATIO) para adopción e integración más simples.

## Implementación y delivery

- **Modelo de venta actual**: Comercialización a grupos que ya tienen infraestructura ATIO; adopción dentro del ecosistema operativo existente.
- **Implementación por marca**: Adaptación de apps Android/iOS (repos separados, branding básico) con tiempo típico ~3 días (assets, builds, tiendas).
- **Branding / personalización básica**: Colores, headers, imágenes, logos, iconos, legales, archivos de configuración (p. ej. Firebase).
- **Build y publicación**: Compilación y envío a App Store y Google Play; cuello de botella operativo citado en el contexto de negocio.

## Arquitectura de producto (conceptual)

- **Core (producto base)**: Funcionalidades estables y reutilizables entre clientes (splash, registro/login según alcance, notificaciones, puntos, canje, estaciones, home, etc.).
- **Alcance estándar**: Lo que el producto incluye por defecto y cómo se delimita frente a opcional y custom.
- **Feature del core (scope)**: Pantallas/vistas que deben existir en todas las implementaciones (splash, legales, home, login, perfil, estaciones, canje, agregar puntos, etc.).
- **Feature opcional**: Puede o no incluirse (p. ej. registro en app, canje por combustible, comercios en tienda de la estación).
- **Feature custom / fuera del core**: Marketplace/delivery, flujos nuevos, integraciones no previstas, cambios en lógica de acumulación o redención; requieren evaluación.
- **Configurable vs custom**: Línea estratégica: priorizar configuración y estándares frente a desarrollos específicos por cliente.

## Experiencia y reglas de cambio

- **Restricciones UI/UX**: Cambios permitidos (marca, textos, legales); limitados (componentes/layout menor); no permitidos (rediseño total, navegación, consistencia del flujo).
- **Anti-patterns**: Tratar cada cliente como producto distinto, divergencias del flujo principal, features aislados sin impacto en el core, que el cliente defina la arquitectura.

## Operación y fricción

- **Cuellos de botella**: Assets sin diseño, múltiples tamaños de imagen, limpieza de logos, builds/tiendas, duplicidad Android/iOS.
- **Solicitudes recurrentes problemáticas**: Cambios al home, flujos distintos, e-commerce/delivery; aumentan variabilidad y esfuerzo.

## Métricas de madurez (citadas en visión)

- **Tracción actual**: Referencia de “más de 15 grupos” implementados como validación de mercado.

## Términos funcionales (lealtad)

- **QR en ticket**: Mecanismo para vincular la compra con el abono de puntos al escanear desde la app.
- **Acumulación / agregar puntos**: Registro de puntos tras compra u operación válida.
- **Canje / redención**: Uso de puntos por recompensas (y variantes opcionales: combustible, comercios en estación).
- **Recompensa**: Beneficio canjeable por puntos (combustible, productos u otros según programa).

## Segmentación (target clients)

- **Segmento primario**: Grupos con varias estaciones, operación consolidada, POS integrado.
- **Segmento secundario (potencial)**: Sin lealtad o con programas poco eficientes; interés en digitalizar relación con cliente.

## Valor para el cliente

- **Retención y recompra**: Objetivos centrales frente a competencia y baja diferenciación en precio/producto.
- **Drivers de valor**: Retención, frecuencia de compra, diferenciación, simplicidad operativa, integración con sistemas existentes.