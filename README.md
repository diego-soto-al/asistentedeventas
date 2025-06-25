# Asistente de ventas para Facebook Marketplace

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

## Customizable
- Editar Modelfile para ajustar a necesidades de usuario

### Requerimientos
- CPU: 4 núcleos
- RAM: 8GB
- Python 3.10+
- Ollama
- llama3.2

### Recomendados
- RAM: 16GB

## Instalación rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/diego-soto-al/asistentedeventas
cd asistentedeventas

# 2. Instalar Ollama y modelo
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
pip install ollama

# 3. Crear modelo
ollama create diego-soto -f DiegoSoto.Modelfile

# 4. Ejecutar codigo
python3 diego.py

