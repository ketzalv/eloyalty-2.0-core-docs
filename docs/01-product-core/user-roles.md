# User Roles - eLoyalty 2.0

## 🎯 Objetivo

Definir los tipos de usuario dentro del sistema eLoyalty 2.0, sus responsabilidades y diferencias de comportamiento, evitando complejidad innecesaria y manteniendo el enfoque en un modelo escalable multi-marca.

---

## 🧱 Principios

- Los roles deben ser **mínimos y necesarios**
- Las diferencias deben resolverse mediante:
  - configuración
  - flags
  - reglas de negocio
- Evitar crear nuevos roles cuando una variación puede resolverse por configuración

---

## 👥 Roles dentro de la App Móvil

### 1. Customer (Cliente)

**Descripción:**
Usuario final que utiliza la app para participar en el programa de lealtad.

**Capacidades:**
- Vincular tarjeta
- Consultar saldo de puntos
- Acumular puntos (scan de ticket)
- Redimir puntos por premios
- Ver estaciones de servicio
- Ver promociones y notificaciones
- Consultar historial de redenciones

**Notas:**
- Es el usuario principal del sistema
- Todos los flujos del core están diseñados alrededor de este rol

---

### 2. Merchant (Comercio)

**Descripción:**
Usuario que representa un comercio afiliado al programa de lealtad.

**Subtipos:**

#### 2.1 Merchant - Normal

**Capacidades:**
- Escanear códigos QR de clientes
- Ejecutar redenciones de puntos
- Validar transacciones de canje

**Flujo principal:**
- Recibe cliente → Escanea QR → Ejecuta canje

---

#### 2.2 Merchant - Gasera

**Capacidades:**
- Escanear códigos QR de clientes
- Acumular puntos a clientes

**Restricciones:**
- ❌ No puede realizar redenciones

**Flujo principal:**
- Recibe cliente → Escanea ticket → Acumula puntos

---

## 🔐 Modelo de Activación de Roles

Los roles se determinan mediante:

```json
{
  "role": "customer | merchant",
  "merchant_type": "normal | gasera"
}