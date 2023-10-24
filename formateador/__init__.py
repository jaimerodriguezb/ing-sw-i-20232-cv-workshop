from comando_formateador import FormateadorComando
from formateador_cursiva import Cursiva
from formateador_monoespacion import Mono

class Compound(FormateadorComando): 
    def __init__(self, text="asdasdasdssa"):
        super().__init__(text)
        self.formatos_texto = []

    def add_format(self, format_text):
        self.formatos_texto.append(format_text)

    def execute(self):
        comp_text = self.text
        for format_text in self.formatos_texto:
            comp_text = format_text.execute(comp_text)
        return comp_text
    
