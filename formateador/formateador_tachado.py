from comando_formateador import FormateadorComando

class Tachado(FormateadorComando):
    def execute(self):
        return "!"+self.texto+"!"
