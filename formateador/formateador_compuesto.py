from comando_formateador import FormateadorComando

class FormateadorCompuesto(FormateadorComando):
    def __init__(self, texto) -> None:
        super().__init__(texto)
        self.formateadores_cl = []

    def add_formateador(self, formateador_cl):
        self.apped(formateador_cl)

    def ejecutar(self):
        for f_cl in self.formateadores_cl:
            self.texto = f_cl(self.texto).ejecutar()
        return self.texto