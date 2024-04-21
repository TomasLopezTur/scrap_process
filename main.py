import nbformat
from nbclient import NotebookClient
import subprocess

def ejecutar_notebook(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)
        
        client = NotebookClient(nb=notebook_content)
        client.execute()

        print(f"Ejecución exitosa del notebook: {notebook_path}")
    except Exception as e:
        print(f"Error al ejecutar el notebook {notebook_path}: {e}")

# Ruta a los notebooks que deseas ejecutar en orden
notebook1_path = "main_bahiaBrava.ipynb"
notebook2_path = "main_bahiaMansa.ipynb"

# Ejecutar el primer notebook
ejecutar_notebook(notebook1_path)

# Ejecutar el segundo notebook
ejecutar_notebook(notebook2_path)

script_path = "union.py"

try:
    completed_process = subprocess.run(["python", script_path], capture_output=True, text=True)
    print("Resultado de la ejecución del script:")
    print(completed_process.stdout)
except Exception as e:
    print(f"Error al ejecutar el script: {e}")

