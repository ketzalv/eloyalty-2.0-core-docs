# Product Scope

## Overview

Este documento define el alcance del producto, estableciendo qué funcionalidades forman parte del core, cuáles son opcionales y cuáles quedan fuera del alcance estándar.

El objetivo es:

- Mantener consistencia en el producto
- Evitar desviaciones innecesarias por cliente
- Facilitar la escalabilidad del sistema
- Definir claramente límites entre configuración y desarrollo custom

---

## Core Features (Siempre incluidos)

Las siguientes pantallas y funcionalidades forman parte del producto base y deben estar presentes en todas las implementaciones:

- Splash View
- Política de privacidad View
- Términos y condiciones View
- Home View
- Login View
- Profile View
- Stations View (listado de estaciones)
- Redeem View (canje de puntos por recompensas)
- Agregar puntos View

---

## Optional Features

Estas funcionalidades pueden incluirse o no dependiendo del cliente:

- Register View  
  (algunos clientes utilizan tarjetas físicas de lealtad)

- Redeem Fuel View  
  (canje de puntos por combustible)

- Merchant View  
  (canje de puntos en tiendas dentro de la estación)

---

## Custom Features (Fuera del Core)

Las siguientes solicitudes se consideran fuera del alcance estándar y requieren evaluación específica:

- Funcionalidades tipo marketplace o delivery (ej. estilo Uber Eats)
- Nuevos flujos completos no contemplados en el producto
- Integraciones externas adicionales no previstas
- Cambios en la lógica principal de acumulación o redención

---

## UI / UX Constraints

Para mantener consistencia y escalabilidad del producto, se establecen las siguientes reglas:

### Cambios permitidos

- Colores (paleta de marca)
- Logos
- Imágenes (assets gráficos)
- Textos
- Contenido legal (términos y políticas)

### Cambios limitados (requieren evaluación)

- Agregar componentes adicionales dentro de pantallas existentes
- Ajustes menores de layout

### Cambios no permitidos

- Rediseño completo de pantallas
- Reestructuración de layouts principales
- Alteración de la arquitectura de navegación
- Cambios que rompan la consistencia del flujo base

---

## Anti-Patterns (Evitar)

Se consideran prácticas no deseadas dentro del producto:

- Personalizar cada cliente como si fuera un producto distinto
- Crear versiones divergentes del flujo principal
- Implementar features aislados sin impacto en el core
- Permitir que el cliente defina la arquitectura del producto

---

## Custom Requests Observed

Se han identificado patrones de solicitudes que tienden a generar desviaciones:

- Modificaciones en la experiencia del Home
- Cambios en el flujo de usuario
- Solicitudes de features tipo e-commerce o delivery

Estas solicitudes deben evaluarse cuidadosamente antes de ser aceptadas.

---

## Strategic Guidelines

Para asegurar la evolución del producto:

- Priorizar configurabilidad sobre desarrollo custom
- Mantener un core sólido y reutilizable
- Evaluar si un requerimiento puede convertirse en feature reusable
- Evitar decisiones que incrementen la complejidad sin beneficio claro

---

## Long-Term Goal

El objetivo es evolucionar hacia un producto:

- Configurable por cliente
- Rápido de implementar
- Consistente en experiencia
- Escalable sin incremento proporcional de esfuerzo