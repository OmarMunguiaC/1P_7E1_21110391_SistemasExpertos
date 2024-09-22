"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 7E1
"""

import sqlite3
import random
import json
import os

class KnowledgeAcquisitionModule:
    def __init__(self):
        # Frases predeterminadas
        self.default_phrases = [
            "Hola",
            "¿En qué puedo ayudarte?",
            "Estoy aquí para responder tus preguntas"
        ]
        
        # Cargar conocimiento desde archivo JSON
        self.knowledge_file = 'knowledge.json'
        self.knowledge = self.load_knowledge_from_json()

    def load_knowledge_from_json(self):
        # Cargar conocimiento desde el archivo JSON o crear uno vacío
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_knowledge_to_json(self):
        # Guardar conocimiento en archivo JSON
        with open(self.knowledge_file, 'w') as file:
            json.dump(self.knowledge, file, indent=4)

    def get_random_phrase(self):
        # Seleccionar una frase aleatoria
        return random.choice(self.default_phrases)

    def add_knowledge(self, question, answer):
        # Añadir nuevo conocimiento al diccionario
        self.knowledge[question.lower()] = answer
        self.save_knowledge_to_json()

    def get_answer(self, question):
        # Buscar la respuesta en el diccionario de conocimiento
        return self.knowledge.get(question.lower(), None)

    def interact(self):
        # Mostrar una frase predeterminada aleatoria
        print(self.get_random_phrase())
        
        while True:
            # Obtener la pregunta del usuario
            question = input("Haz tu pregunta (o escribe 'salir' para terminar): ").strip()
            
            if question.lower() == 'salir':
                print("¡Hasta luego!")
                break

            # Buscar la respuesta en el conocimiento existente
            answer = self.get_answer(question)

            if answer:
                print(f"Respuesta: {answer}")
            else:
                # Si no se encuentra la respuesta, preguntar al usuario
                print("No tengo una respuesta para esa pregunta.")
                new_answer = input("¿Qué debería responder a esta pregunta?: ").strip()

                if new_answer:
                    # Guardar el nuevo conocimiento
                    self.add_knowledge(question, new_answer)
                    print("Gracias, he aprendido algo nuevo.")
                else:
                    print("No se agregó una respuesta.")

# Uso
if __name__ == "__main__":
    module = KnowledgeAcquisitionModule()
    module.interact()
