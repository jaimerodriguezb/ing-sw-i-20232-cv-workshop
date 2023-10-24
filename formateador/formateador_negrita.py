from comando_formateador import FormateadorComando

class Negrita(FormateadorComando):
    def execute(self):
        return "*{}*".format(self.texto)