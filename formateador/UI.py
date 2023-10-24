from formateador_negrita import Negrita
from formateador_monoespacio import Mono
from formateador_cursiva import Cursiva
from formateador_subrayo import Subrayo
from formateador_tachado import Tachado
from formateador_compuesto import FormateadorCompuesto

formated_text = ''
text = input("Type a text: ")
frmt = int(input("""Pick the format:
1 - Negrita
2 - Monoespacio
3 - Cursiva
4 - Subrayo
5 - Tachado
6 - Compuesto
"""))

if frmt == 1:
	formated_text = Negrita(text).execute()
elif frmt == 2:
	formated_text = Mono(text).execute()
elif frmt == 3:
	formated_text = Cursiva(text).execute()
elif frmt == 4:
	formated_text = Subrayo(text).execute()
elif frmt == 5:
	formated_text = Tachado(text).execute()
elif frmt == 6:
	bold_cursive = FormateadorCompuesto(text)
	bold_cursive.add_formateador(Negrita(text))
	bold_cursive.add_formateador(Cursiva(text))
	formated_text = bold_cursive.execute()
else:
	print("Try it again :/")

print("\n" + formated_text)