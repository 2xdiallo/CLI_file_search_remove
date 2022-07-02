"""
    Program written in Python 3.7.3 which search or remove a file with a given extension from a specific folder .

    Author : 2xdiallo
    Link_Github: https://github.com/2xdiallo/CLI_file_search_remove.git

    Returns:
        None: None
"""


from pathlib import Path
from pickle import TRUE
import time
from tkinter.font import BOLD
from turtle import bgcolor
from click import command

import typer


chemin_data = Path(__file__).parent / "data"
app = typer.Typer()


def main(ext:str= ".txt",chemin_dossier: str = typer.Argument(None,help="Dossier dans le quel chercher . "), remove:bool = False):
    
    """ Lancer l'appl """
    # 
    #     Lancer l'appli 

    # Args:
    #     ext (str, optional):  l'extension que vous vous voulez rechercher    . Defaults to ".txt".
    #     chemin_dossier (str, optional): Le chemin du dossier dont vous voulez faire quela recherche des fichiers soit faites  .... Defaults to typer.Argument(None,help="Dossier dans le quel chercher . ").
    #     remove (bool, optional): Accepter la suppression des fichiers. Defaults to False.
    # 
    
    if not chemin_dossier:
        chemin_dossier = chemin_data
        chemin_each_dossier = get_files_with_extension(extension=ext)
        for chemin in chemin_each_dossier:
            print(chemin,"\n")
    else:
        chemin_dossier = Path(chemin_dossier)
        print(chemin_dossier)
        chemin_each_dossier = get_files_with_extension(extension=ext,chemin_dossiers = chemin_dossier)
        
        with typer.progressbar(chemin_each_dossier) as progress:
            for chemin in progress:
                time.sleep(0.1)
                print("\n",chemin,"\n")

def get_files_with_extension(extension : str = ".txt",chemin_dossiers: str = chemin_data) -> list:
    """l'extension que vous vous voulez rechercher ...

    Args:
        extension (str, optional): Le chemin du dossier dont vous voulez faire quela recherche des fichiers soit faites  . Defaults to ".txt".
        chemin_dossiers (str, optional): Le chemin du dossier dont vous voulez faire quela recherche des fichiers soit faites. Defaults to chemin_data.

    Returns:
        list: return une liste de fichier contenu dans le dossier 
    """
    chemin_dossiers = Path(chemin_dossiers)
    liste_files = [file.absolute() for file in chemin_dossiers.iterdir() if file.is_file and (file.suffix == extension)  ] #list comprehension       
    return liste_files            
            
def delete_file_with_extension(extension:str = ".txt",chemin:str = chemin_data,remove:bool = False ):
    liste_files = get_files_with_extension(extension=extension,chemin_dossiers=chemin)
    print(f"\n Tous les fichiers {extension} dans ce dossier sont : \n ")
    for i in liste_files:
        print(i,"\n")
    for file in liste_files:
        if remove:
            p = Path(file)
            choix = typer.confirm(f"Voulez vous vraiment supprimer {p.name} ")
            print(choix)
            if choix == True:
                p.unlink()
                typer.echo(f"le fichier  {p.name} a ete  bien supprime ... ")
            else :
                typer.echo(f"la suppression de {p.name} a ete annule ...")
    

@app.command()
def search(extension: str, chemin: str):
    """ Les fichiers que vous vous voulez rechercher ...

    Args:
        extension (str): l'extension que vous vous voulez rechercher ...        
    """
    main(ext = extension,chemin_dossier=chemin)

@app.command()
def remove(extension: str,chemin: str):
    """ Supprimer les fichiers 

    Args:
        extension (str): L'extension que vous vous voulez supprimer ... 
    """
    delete_file_with_extension(extension= extension,chemin=chemin, remove = True)

@app.command()
def info():
    """Usage: main.py search ".txt" C:\ or main.py remove ".txt" C:\  
    """
    typer.secho("Usage_example: \n main.py search '.txt' C:\ \n  main.py remove '.txt' C:\  ",fg=typer.colors.BRIGHT_GREEN)

if __name__ == "__main__":
    app()
    
   