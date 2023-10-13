class FormateadorComando:
    def __init__(self, texto) -> None:
        self.texto = texto

    def ejecutar(self):
        raise NotImplementedError('Este metodo debe ser implemantado')
