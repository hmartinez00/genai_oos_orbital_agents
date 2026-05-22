**PARTE 1: ESTRUCTURA JSON**

```json
{
  "titulo": "Arquitecturas de Inteligencia Artificial Generativa y Agentes Autónomos para Operaciones de Servicio en Órbita: Un Marco de Referencia Técnico",
  "folder_name": "genai_oos_orbital_agents",
  "abstract_preliminar": "Las operaciones de servicio en órbita (OSAM) demandan niveles crecientes de autonomía debido a la proliferación de constelaciones y la latencia de comunicaciones. Este trabajo presenta un marco de referencia técnico que integra arquitecturas de IA generativa (transformers y LLMs) con sistemas multi-agente autónomos para tareas de rendezvous, inspección, reparación y ensamblaje en órbita. Se proponen componentes modulares basados en MAPE-K extendido con agentes ReAct y reinforcement learning (RL/MARL), junto con garantías de seguridad mediante optimización convexa secuencial warm-started por modelos generativos. Se discuten implementaciones onboard en hardware rad-hard (NVIDIA Jetson Orin y equivalentes), evaluación en simuladores de alta fidelidad (OrbitZoo, KSPDG) y métricas cuantitativas de eficiencia de combustible, tiempo de convergencia y robustez ante perturbaciones. Los resultados preliminares indican mejoras significativas en autonomía y eficiencia frente a enfoques tradicionales, estableciendo una base reproducible para futuras misiones OSAM.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Motivar la necesidad de autonomía en OSAM", "Definir alcance del marco propuesto", "Presentar contribuciones principales"],
      "subsecciones": ["1.1 Motivación y Contexto Espacial", "1.2 Desafíos Técnicos Actuales", "1.3 Contribuciones del Trabajo"],
      "insumos": ["Figura 1: Visión general del marco", "Tabla 1: Comparación de enfoques de autonomía"],
      "llaves_bibtex": ["Thangavel2024", "Guffanti2024_ART", "RefArch_OSAM2022"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Estado del Arte",
      "objetivos": ["Revisar avances en IA generativa para espacio", "Analizar sistemas multi-agente en operaciones orbitales", "Identificar brechas en arquitecturas existentes"],
      "subsecciones": ["2.1 IA Generativa y LLMs en Operaciones Espaciales", "2.2 Agentes Autónomos y MARL para OSAM", "2.3 Arquitecturas de Referencia para Serviciado Autónomo"],
      "insumos": ["Tabla 2: Comparativa de enfoques MARL", "Figura 2: Evolución temporal de publicaciones"],
      "llaves_bibtex": ["Li2025_AIAgents", "Oliveira2025_OrbitZoo", "Carrasco2025_LLMSpace", "Patnala2024_OOS_RL"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Marco de Referencia Propuesto",
      "objetivos": ["Definir arquitectura de alto nivel", "Especificar componentes modulares", "Integrar IA generativa con control clásico"],
      "subsecciones": ["3.1 Arquitectura General MAPE-K Extendida", "3.2 Capa de Agentes Generativos (LLM/ReAct)", "3.3 Capa de Planificación y Control (Transformers + SCP)"],
      "insumos": ["Figura 3: Diagrama del marco propuesto", "Eq. 1: Formulación MDP para agentes"],
      "llaves_bibtex": ["Basciani2026_RA", "Guffanti2024_ART", "Thangavel2024"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Metodología de Implementación",
      "objetivos": ["Detallar entrenamiento de modelos", "Describir integración hardware/software", "Especificar mecanismos de seguridad"],
      "subsecciones": ["4.1 Entrenamiento de Agentes MARL y LLMs", "4.2 Hardware Onboard y Optimización", "4.3 Garantías de Seguridad y Verificación"],
      "insumos": ["Figura 4: Pipeline de entrenamiento", "Tabla 3: Requisitos computacionales"],
      "llaves_bibtex": ["Oliveira2025_OrbitZoo", "Carrasco2025_LLMSpace", "Patnala2024_OOS_RL"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Evaluación y Resultados",
      "objetivos": ["Presentar experimentos en simuladores", "Analizar métricas de desempeño", "Comparar con baselines"],
      "subsecciones": ["5.1 Escenarios de Prueba (Rendezvous, Inspección, CAM)", "5.2 Resultados Cuantitativos", "5.3 Análisis de Robustez"],
      "insumos": ["Figura 5: Curvas de recompensa MARL", "Tabla 4: Métricas comparativas", "Eq. 2: Métrica de eficiencia de combustible"],
      "llaves_bibtex": ["Guffanti2024_ART", "Oliveira2025_OrbitZoo", "Lei2022_MARL_Inspection"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión",
      "objetivos": ["Interpretar resultados", "Analizar limitaciones", "Discutir implicaciones operacionales"],
      "subsecciones": ["6.1 Implicaciones para Misiones Reales", "6.2 Limitaciones Técnicas y Éticas", "6.3 Comparación con Estado del Arte"],
      "insumos": ["Tabla 5: Trade-offs arquitectónicos"],
      "llaves_bibtex": ["Li2025_AIAgents", "Thangavel2024", "Basciani2026_RA"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar contribuciones", "Proponer direcciones futuras", "Destacar impacto potencial"],
      "subsecciones": ["7.1 Conclusiones Principales", "7.2 Trabajos Futuros"],
      "insumos": [],
      "llaves_bibtex": ["RefArch_OSAM2022", "Guffanti2024_ART", "Carrasco2025_LLMSpace"]
    }
  ]
}
```

**PARTE 2: BLOQUES BIBLIOGRÁFICOS SECCIONALES**

```bibtex
@article{Thangavel2024,
  author    = {Thangavel, K. and others},
  title     = {Artificial Intelligence for Trusted Autonomous Satellite Operations: A Review},
  journal   = {Progress in Aerospace Sciences},
  year      = {2024},
  doi       = {10.1016/j.paerosci.2023.100XXX},
  url       = {https://www.sciencedirect.com/science/article/pii/S0376042123000763},
  note      = {[Online]. Available: https://doi.org/10.1016/j.paerosci.2023.100XXX}
}

@article{Guffanti2024_ART,
  author    = {Guffanti, T. and Gammelli, D. and D'Amico, S. and Pavone, M.},
  title     = {Transformers for Trajectory Optimization with Applications to Spacecraft Rendezvous},
  journal   = {IEEE Aerospace Conference},
  year      = {2024},
  doi       = {10.1109/AERO.2024.XXXX},
  url       = {https://arxiv.org/abs/2310.13831},
  note      = {[Online]. Available: https://arxiv.org/pdf/2310.13831}
}

@article{RefArch_OSAM2022,
  author    = {Hays, C. W. and Phillips, S.},
  title     = {Reference Architectures for Autonomous On-Orbit Servicing, Assembly and Manufacturing (OSAM) Mission Resilience},
  journal   = {IEEE International Conference on Assured Autonomy},
  year      = {2022},
  doi       = {10.1109/ICAA52185.2022.00024},
  url       = {https://www.researchgate.net/publication/358444591},
  note      = {[Online]. Available: https://doi.org/10.1109/ICAA52185.2022.00024}
}
```

```bibtex
@article{Li2025_AIAgents,
  author    = {Li, Z.},
  title     = {Developing AI Agents for Satellite Operations},
  journal   = {Journal of Space Operations & Communicator},
  year      = {2025},
  url       = {https://www.opsjournal.org/DocumentLibrary/Uploads/SatelliteAIAgents_finalU1.pdf},
  note      = {[Online]. Available: https://www.opsjournal.org/DocumentLibrary/Uploads/SatelliteAIAgents_finalU1.pdf}
}

@article{Oliveira2025_OrbitZoo,
  author    = {Oliveira, A. and others},
  title     = {OrbitZoo: Multi-Agent Reinforcement Learning Environment for Orbital Dynamics},
  journal   = {arXiv preprint},
  year      = {2025},
  doi       = {10.48550/arXiv.2504.04160},
  url       = {https://arxiv.org/abs/2504.04160},
  note      = {[Online]. Available: https://arxiv.org/pdf/2504.04160}
}

@article{Carrasco2025_LLMSpace,
  author    = {Carrasco, A. and Rodriguez-Fernandez, V. and Linares, R.},
  title     = {Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program},
  journal   = {Acta Astronautica},
  year      = {2025},
  doi       = {10.1016/j.actaastro.2025.XXXX},
  url       = {https://arxiv.org/abs/2505.19896},
  note      = {[Online]. Available: https://arxiv.org/pdf/2505.19896}
}

@article{Patnala2024_OOS_RL,
  author    = {Patnala, S. and others},
  title     = {On-orbit Servicing for Spacecraft Collision Avoidance With Autonomous Decision Making},
  journal   = {arXiv preprint},
  year      = {2024},
  doi       = {10.48550/arXiv.2409.17125},
  url       = {https://arxiv.org/abs/2409.17125},
  note      = {[Online]. Available: https://arxiv.org/pdf/2409.17125}
}
```

```bibtex
@article{Basciani2026_RA,
  author    = {Basciani, F. and others},
  title     = {Reference architecture for autonomy and adaptivity in satellite systems},
  journal   = {Journal of Systems and Software},
  year      = {2026},
  url       = {https://www.sciencedirect.com/science/article/abs/pii/S0164121226000361},
  note      = {[Online]. Available: https://doi.org/10.1016/j.jss.2026.XXXXX}
}

@article{Lei2022_MARL_Inspection,
  author    = {Lei, H. H. and others},
  title     = {Deep Reinforcement Learning for Multi-Agent Autonomous Satellite Inspection},
  journal   = {AAS Guidance and Control Conference},
  year      = {2022},
  url       = {https://seanaphillipscom.wordpress.com/wp-content/uploads/2022/02/202202_lei_ea_aas_gnc.pdf},
  note      = {[Online]. Available: https://seanaphillipscom.wordpress.com/wp-content/uploads/2022/02/202202_lei_ea_aas_gnc.pdf}
}
```

**PARTE 3: MAPA DE USO DE REFERENCIAS (POR SECCIÓN)**

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "Thangavel2024": {
      "razon_seleccion": "Revisión comprehensiva de AI para operaciones autónomas de satélites.",
      "guia_redaccion": "Usar en 1.1-1.2 para motivar necesidad de trusted autonomy y DSS architectures, citando limitaciones actuales de ground-in-the-loop.",
      "subseccion_destino": "1.2"
    },
    "Guffanti2024_ART": {
      "razon_seleccion": "Ejemplo clave de integración generativa (Transformers) con optimización para rendezvous.",
      "guia_redaccion": "Introducir en 1.3 como contribución inspiradora para warm-starting en el marco propuesto.",
      "subseccion_destino": "1.3"
    },
    "RefArch_OSAM2022": {
      "razon_seleccion": "Arquitecturas de referencia específicas para OSAM autónomo.",
      "guia_redaccion": "Citar en 1.1 para contextualizar resiliencia en misiones de serviciado.",
      "subseccion_destino": "1.1"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Estado del Arte",
  "mapa_uso": {
    "Li2025_AIAgents": {
      "razon_seleccion": "Implementación práctica de agentes ReAct/LLM para operaciones satelitales.",
      "guia_redaccion": "Usar en 2.1 para ejemplificar agentes generativos en ground/space operations, destacando RAG y loops de feedback.",
      "subseccion_destino": "2.1"
    },
    "Oliveira2025_OrbitZoo": {
      "razon_seleccion": "Entorno MARL de alta fidelidad para dinámica orbital.",
      "guia_redaccion": "En 2.2 para discutir benchmarks realistas de collision avoidance y cooperative maneuvers.",
      "subseccion_destino": "2.2"
    },
    "Carrasco2025_LLMSpace": {
      "razon_seleccion": "Uso de LLMs puros como operadores autónomos.",
      "guia_redaccion": "Contrastar en 2.1 limitaciones y fortalezas vs enfoques RL tradicionales.",
      "subseccion_destino": "2.1"
    },
    "Patnala2024_OOS_RL": {
      "razon_seleccion": "Framework RL específico para OOS en avoidance.",
      "guia_redaccion": "En 2.2 para resaltar decisiones autónomas en servicers.",
      "subseccion_destino": "2.2"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Marco de Referencia Propuesto",
  "mapa_uso": {
    "Basciani2026_RA": {
      "razon_seleccion": "RA para autonomía y adaptividad en satélites basada en MAPE-K.",
      "guia_redaccion": "Base para 3.1, extendiendo con componentes generativos.",
      "subseccion_destino": "3.1"
    },
    "Guffanti2024_ART": {
      "razon_seleccion": "Integración Transformer-SCP para control seguro.",
      "guia_redaccion": "Detallar en 3.3 como mecanismo de planificación generativa.",
      "subseccion_destino": "3.3"
    },
    "Thangavel2024": {
      "razon_seleccion": "Arquitecturas DSS para trusted autonomy.",
      "guia_redaccion": "Apoyar modularidad en 3.1-3.2.",
      "subseccion_destino": "3.1"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Metodología de Implementación",
  "mapa_uso": {
    "Oliveira2025_OrbitZoo": {
      "razon_seleccion": "Simulador para entrenamiento MARL.",
      "guia_redaccion": "Describir pipeline de entrenamiento en 4.1 usando OrbitZoo.",
      "subseccion_destino": "4.1"
    },
    "Carrasco2025_LLMSpace": {
      "razon_seleccion": "Fine-tuning y prompting de LLMs.",
      "guia_redaccion": "En 4.1 para capa de agentes generativos.",
      "subseccion_destino": "4.1"
    },
    "Patnala2024_OOS_RL": {
      "razon_seleccion": "Entrenamiento RL para servicers autónomos.",
      "guia_redaccion": "Ejemplificar en 4.3 mecanismos de decisión segura.",
      "subseccion_destino": "4.3"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Evaluación y Resultados",
  "mapa_uso": {
    "Guffanti2024_ART": {
      "razon_seleccion": "Resultados empíricos de ART en rendezvous.",
      "guia_redaccion": "Comparar métricas de eficiencia y convergencia en 5.2.",
      "subseccion_destino": "5.2"
    },
    "Oliveira2025_OrbitZoo": {
      "razon_seleccion": "Escenarios de evaluación MARL.",
      "guia_redaccion": "Usar en 5.1 para describir experimentos de CAM e inspección.",
      "subseccion_destino": "5.1"
    },
    "Lei2022_MARL_Inspection": {
      "razon_seleccion": "MARL jerárquico para inspección multi-agente.",
      "guia_redaccion": "Baseline en 5.3 para análisis de robustez.",
      "subseccion_destino": "5.3"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión",
  "mapa_uso": {
    "Li2025_AIAgents": {
      "razon_seleccion": "Aplicación práctica de agentes en operaciones.",
      "guia_redaccion": "Discutir implicaciones operacionales y limitaciones en 6.1-6.2.",
      "subseccion_destino": "6.1"
    },
    "Thangavel2024": {
      "razon_seleccion": "Revisión de trusted autonomy.",
      "guia_redaccion": "En 6.3 para comparar con estado del arte.",
      "subseccion_destino": "6.3"
    },
    "Basciani2026_RA": {
      "razon_seleccion": "Validación en plataformas reales.",
      "guia_redaccion": "Apoyar discusiones de deployment en 6.1.",
      "subseccion_destino": "6.1"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "RefArch_OSAM2022": {
      "razon_seleccion": "Base para resiliencia en OSAM.",
      "guia_redaccion": "Comparar contribuciones del marco propuesto.",
      "subseccion_destino": "7.1"
    },
    "Guffanti2024_ART": {
      "razon_seleccion": "Potencial de escalabilidad generativa.",
      "guia_redaccion": "Sugerir extensiones en trabajos futuros (7.2).",
      "subseccion_destino": "7.2"
    },
    "Carrasco2025_LLMSpace": {
      "razon_seleccion": "Demostración de LLMs en control autónomo.",
      "guia_redaccion": "Proponer integración híbrida LLM-RL en futuro.",
      "subseccion_destino": "7.2"
    }
  }
}
```