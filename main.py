#!/usr/bin/env python3

import subprocess
import sys
import os
from InquirerPy import prompt, inquirer
from InquirerPy.exceptions import InvalidArgument

def run_cmd(cmd):
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando: {' '.join(cmd)}", file=sys.stderr)
        print(f"   Codigo de salida: {e.returncode}", file=sys.stderr)
        print(f"   Error: {e.stderr.strip()}", file=sys.stderr)
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(f"Comando no encontrado: {cmd[0]}. Esta instalado?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}", file=sys.stderr)
        sys.exit(1)


def pk_install(*packages):
    if not packages:
        print("Uso: pk install <paquete1> [paquete2] ...")
        sys.exit(1)
    cmd = ["sudo", "xbps-install", "-y"] + list(packages)
    print(f"Instalando: {' '.join(packages)}")
    run_cmd(cmd)

def pk_remove(*packages):
    if not packages:
        print("Uso: pk remove <paquete1> [paquete2] ...")
        sys.exit(1)
    cmd = ["sudo", "xbps-remove", "-y"] + list(packages)
    print(f"Eliminando: {' '.join(packages)}")
    run_cmd(cmd)

def pk_query(pattern=None):
    if pattern:
        cmd = ["xbps-query", "-Rs", pattern]
        print(f"Buscando paquetes que coincidan con: '{pattern}'")
    else:
        cmd = ["xbps-query", "-l"]
        print("Paquetes instalados:")
    run_cmd(cmd)

def pk_up():
    print("Actualizando todo el sistema: xbps-install -Syu")
    run_cmd(["sudo", "xbps-install", "-Syu"])

def main_menu():
    custom_style = {
        "qmark": "bold",
        "pointer": "bold",
    }
    while True:
        try:
            questions = [
                {
                    "type": "list",
                    "message": "Selecciona una accion:",
                    "choices": [
                        "Instalar paquetes",
                        "Eliminar paquetes",
                        "Buscar o listar paquetes",
                        "Actualizar todo el sistema",
                        "Salir"
                    ],
                    "name": "action",
                }
            ]

            result = prompt(questions, style=custom_style)
            action = result["action"]

            if action == "Instalar paquetes":
                package_input = inquirer.text(message="Ingresa los paquetes a instalar (separados por espacio):").execute()
                packages = package_input.split()
                if packages:
                    pk_install(*packages)
            elif action == "Eliminar paquetes":
                package_input = inquirer.text(message="Ingresa los paquetes a eliminar (separados por espacio):").execute()
                packages = package_input.split()
                if packages:
                    pk_remove(*packages)
            elif action == "Buscar o listar paquetes":
                pattern = inquirer.text(message="Ingresa un patron de busqueda (deja vacio para listar instalados):").execute()
                pk_query(pattern)
            elif action == "Actualizar todo el sistema":
                pk_up()
            elif action == "Salir":
                print("Hasta luego!")
                break

        except KeyboardInterrupt:
            print("\nOperacion cancelada por el usuario. Saliendo.")
            break
        except InvalidArgument as e:
            print(f"Error en la seleccion: {e}", file=sys.stderr)

if __name__ == "__main__":
    main_menu()
