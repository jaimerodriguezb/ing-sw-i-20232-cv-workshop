from comando_formateador import FormateadorComando

class Subrayo(FormateadorComando):
    def execute(self):
        return "*~~*".format(self.texto)