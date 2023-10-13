from comando_formateador import FormateadorComando

class Cursiva(FormateadorComando):
   def execute(self):
    return "_{}_".format(self.text)
