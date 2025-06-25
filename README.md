# Asistente Diego Soto para Facebook Marketplace

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-v0.1.37+-orange.svg)
![Model](https://img.shields.io/badge/Model-llama3.2-green.svg)

Asistente conversacional especializado en ventas por Facebook Marketplace con identidad chilena.

## Características clave
- Responde exclusivamente en español
- Calcula descuentos del 15% automáticamente
- Entrega solo en Metro República
- Respuestas ultra-breves (<12 palabras)
- Mantiene consistencia en negociaciones

##  Requisitos técnicos

### Mínimos
- CPU: 4 núcleos (x86_64 con AVX)
- RAM: 8GB
- Docker o Python 3.10+

### Recomendados
- RAM: 16GB
- GPU: NVIDIA con 6GB+ VRAM (opcional)

## Instalación rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/tuusuario/asistente-diego.git
cd asistente-diego

# 2. Construir con Docker (recomendado)
docker build -t diego-assistant .

# 3. Ejecutar
docker run -it --rm diego-assistant
