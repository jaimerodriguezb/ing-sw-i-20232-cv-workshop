from comando_formateador import FormateadorComando

class Mono(FormateadorComando):
    def execute(self):
        return "```{}```".format(self.texto)