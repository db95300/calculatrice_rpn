# Calculatrice RPN avec FastAPI

Ce projet est une API RESTful qui implémente une calculatrice en utilisant la notation polonaise inversée (RPN). Développée avec FastAPI, l'API est conçue pour effectuer des opérations arithmétiques de base telles que l'addition, la soustraction, la multiplication et la division.

## Fonctionnalités

- Ajout d'un élément à la pile.
- Récupération de l'état actuel de la pile.
- Nettoyage de la pile.
- Opération d'addition, de soustraction, de multiplication et de division.

## Prérequis

- Python 3.9 ou supérieur.

## Installation

Pour installer les dépendances nécessaires au fonctionnement de l'API, suivez ces étapes :

1. Clonez le dépôt ou téléchargez les fichiers.
2. Installez les dépendances en exécutant :

pip install -r requirements.txt

## Démarrage de l'application éxécuter: 

uvicorn main:app --reload

L'API sera accessible à http://127.0.0.1:8000. L'interface utilisateur de Swagger pour tester l'API se trouve à http://127.0.0.1:8000/docs.