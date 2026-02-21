
# Flujo
input → extracción → comparación → reporte
## Tema central
**Diseño e implementación de un framework modular para auditoría de seguridad en sistemas Linux (SentinelLinux).**

---

## Contexto del problema
- Los sistemas Linux son ampliamente utilizados en servidores, infraestructuras críticas y entornos corporativos.  
- La auditoría de seguridad en Linux suele ser compleja, poco automatizada y dependiente de revisiones manuales.  
- Herramientas existentes como **Lynis, OpenVAS o Nmap** presentan limitaciones: requieren conocimientos avanzados, no siempre son modulares y generan reportes poco adaptados.  
- Esto dificulta la detección eficiente de vulnerabilidades, configuraciones inseguras y permisos inadecuados.  

---

## Problema de investigación
¿De qué manera puede mejorarse la auditoría de seguridad en sistemas Linux, considerando que los procesos actuales son complejos, poco automatizados, carecen de modularidad y generan reportes que no siempre se adaptan a las necesidades de administradores y auditores?

---

## Objetivo general
Desarrollar un framework modular orientado a la auditoría de seguridad en sistemas Linux, capaz de automatizar la identificación de vulnerabilidades, configuraciones inseguras y permisos inadecuados, ofreciendo reportes claros y personalizables para apoyar la gestión de la seguridad informática.

*(Se evita repetir “diseñar” e “implementar”, pero se mantiene el sentido académico y técnico.)*

---

## Objetivos específicos (ejemplos)
1. Crear módulos independientes para revisar permisos, usuarios, servicios activos y configuraciones críticas.  
2. Automatizar la detección de vulnerabilidades y malas configuraciones en sistemas Linux.  
3. Generar reportes en formatos personalizables (JSON, HTML, Markdown) que incluyan hallazgos técnicos y su relación con normativas.  
4. Validar el framework en diferentes distribuciones Linux y comparar resultados con herramientas similares como Lynis.  
5. Documentar el diseño, metodología y resultados, aportando un modelo replicable y extensible.  

---

## Posibles resultados
1. Obtención de un framework modular funcional para auditorías de seguridad en Linux.  
2. Generación de reportes claros y adaptados a las necesidades de administradores y auditores.  
3. Validación del framework en entornos reales, demostrando su eficacia frente a herramientas existentes.  
4. Contribución académica mediante documentación y propuesta metodológica.  
5. Propuesta de mejoras futuras: integración con bases de datos de vulnerabilidades (CVE/NVD), monitoreo continuo, automatización de mitigaciones básicas.  

---

## Proyectos similares y aprendizajes
### Lynis
- Herramienta reconocida para auditoría de seguridad en Linux.  
- Ventajas: amplia cobertura de pruebas, integración con sistemas de gestión de seguridad.  
- Limitaciones: reportes poco personalizables, curva de aprendizaje alta, no modular (ejecuta auditorías completas sin segmentación).  
- **Qué agregar al framework SentinelLinux:**  
  - Modularidad real (activar/desactivar módulos según necesidad).  
  - Reportes adaptados a normativas.  
  - Extensibilidad para que otros investigadores añadan módulos.  
  - Interfaz más clara y resultados estructurados.  

---

## Normativas relevantes
### PCI-DSS
- Requisitos para proteger datos de tarjetas.  
- Parámetros aplicables: deshabilitar servicios innecesarios, cifrado de datos, segmentación de red.  

### HIPAA
- Normativa para proteger datos médicos.  
- Parámetros aplicables: permisos de archivos sensibles, auditoría de accesos, autenticación fuerte.  

### ISO/IEC 27001
- Estándar internacional de gestión de seguridad de la información.  
- Parámetros aplicables: gestión de usuarios, políticas de contraseñas, protección de logs, gestión de vulnerabilidades.  

### Uso en el framework
- **Definir parámetros técnicos**: traducir requisitos normativos a configuraciones Linux (ej. permisos de `/etc/shadow`).  
- **Mapear hallazgos a controles normativos**: cada hallazgo se relaciona con un control específico de PCI-DSS, HIPAA o ISO27001.  
- **Generar reportes normativos**: incluir secciones como *Hallazgo → Control afectado → Norma de referencia*.  
- **Validez académica y práctica**: el framework no solo detecta problemas técnicos, sino que demuestra cumplimiento normativo.  

---

## Conclusión del resumen
El proyecto **SentinelLinux** se diferencia de herramientas existentes como Lynis al ofrecer un **framework modular, extensible y normativamente alineado**. Su aporte principal es combinar **automatización técnica** con **validez académica y normativa**, generando reportes claros que vinculan hallazgos con estándares internacionales de seguridad.


