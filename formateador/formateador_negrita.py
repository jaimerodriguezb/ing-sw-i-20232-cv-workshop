from comando_formateador import FormateadorComando

class Negrita(FormateadorComando):
    def __init__(self, texto) -> None:
        super().__init__(texto)
    def execute(self):
        return "*{}*".format(self.texto)