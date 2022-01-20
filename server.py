from flask import Flask, render_template

app = Flask( __name__ )

usuarios = [{
    "nombre" : "Alex",
    "apellido" : "Martinez",
    "id" : 123
},
{
    "nombre" : "Martha",
    "apellido" : "Sanchez",
    "id" : 456
},
{
    "nombre" : "Ruben",
    "apellido" : "Castillo",
    "id" : 789
}]

@app.route( '/', methods=['GET'] )
def paginaInicial():
    hobbies = [ "Programar", "Leer", "Video Juegos", "Cantar" ]
    return render_template( "index.html", nombre="Alex", apellido="Martinez", lista=hobbies )

@app.route( '/datos/<nombre>/<apellido>', methods=['GET'] )
def imprimeDatos( nombre, apellido ):
    print( nombre )
    print( apellido )
    return "<h1> Estos son los datos de " + nombre + " " + apellido + "</h1>"

@app.route( '/usuarios/<int:id>', methods=['GET'])
def imprimeInformacionDeUsuario( id ):
    print( type( id ) )
    usuarioEncontrado = None
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarioEncontrado = usuario
    return render_template( "usuario.html", usuario=usuarioEncontrado, id=id )


if __name__ == "__main__":
    app.run( debug=True )