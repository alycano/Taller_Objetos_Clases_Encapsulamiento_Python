class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return "El libro ha sido prestado"
        else:
            return "El libro no esta disponible"

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return "El libro ha sido devuelto"
        else:
            return "El libro ya estaba en la biblioteca"

    def informacion(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
            
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}, Estado: {estado}"

# Pruebas del taller
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

print(libro1.informacion())
print(libro1.prestar())
print(libro1.prestar()) # Intento prestarlo otra vez
print(libro1.informacion())
print(libro1.devolver())
print(libro1.informacion())