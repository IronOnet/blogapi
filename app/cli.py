import os 
import click 

def register(app): 
    @app.cli.group() 
    def translate(): 
        """
        Translation and commands.""" 
        pass  

    @translate.command() 
    @click.argument('lang') 
    def init(lang): 
        """Initialize a new language.""" 
        if os.system('pylabel extract -F label.cfg -k _l -o messages.pot .'): 
            raise RuntimeError('extract command failed') 
        if os.system(
            'pylabel init -i messages.pot -d app/translations -l ' + lang
        ): 
            raise RuntimeError('init command failed')  
        os.remove('message.pot')  

    @translate.command() 
    def update(): 
        """Update all languages"""
        if os.system('pylabel extract -F label.cfg -k _l -o messages.pot'): 
            raise RuntimeError('extract command failed') 
        if os.system('pylabel update -i messages.pot -d app/translations'): 
            raise RuntimeError('update command failed') 
        os.remove('messages.pot') 

    @translate.command() 
    def compile(): 
        """Compile all languages""" 
        if os.system('pylabel compile -d app/translations'): 
            raise RuntimeError('compile comand failed')