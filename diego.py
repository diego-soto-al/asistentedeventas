#Autor: Diego Soto Almendras
#USACH primer semestre 2025



from ollama import chat

def cargar_publicacion():
    """Permite al usuario ingresar la publicación manualmente"""
    print("\n" + "="*50)
    print("Ingresa la publicación de Facebook Marketplace (termina con 'fin' en una línea separada):")
    print("="*50)
    
    lineas = []
    while True:
        linea = input()
        if linea.lower() == 'fin':
            break
        lineas.append(linea)
    
    return "\n".join(lineas)

def main():
 
    print("Asistente Diego Soto - Facebook Marketplace")
    print("Cargando modelo...")
    
    # Cargar publicación interactivamente
    post = cargar_publicacion()
    
    # Contexto inicial con la publicación
    messages = [
        {
            'role': 'user',
            'content': f"PUBLICACIÓN ACTUAL: Recuerda seguir estrictamente las reglas asignadas\n{post}"
        },
        {
            'role': 'assistant',
            'content': "Entendido, tengo la publicación. ¿En qué puedo ayudarte?"
        }
    ]
    
    print("\nPublicación cargada:")
    print("="*50)
    print(post)
    print("="*50)
    print("Escribe 'salir' para terminar\n")
    
    # Bucle de conversación
    while True:
        user_input = input("Cliente: ")
        
        if user_input.lower() in ['salir', 'exit']:
            break
            
        # Añadir mensaje del usuario
        messages.append({'role': 'user', 'content': user_input})
        
        try:
            # Obtener respuesta del modelo
            response = chat(
                model='diego-soto',
                messages=messages,
                options={
                    'temperature': 0.2,
                    'num_ctx': 4096,
                    'seed': 42
                }
            )
            
            respuesta = response['message']['content']
            print(f"\nDiego Soto: {respuesta}")
            
            # Añadir respuesta al historial
            messages.append({'role': 'assistant', 'content': respuesta})
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
