from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """

"""

def index(request):
    estudiantes = [ 'Isabella Caballero',
                    'Alejandro Hermitaño', 
                    'Joan Palomino', 
                    'Pierre Bernaola', 
                    'Fabricio Condori', 
                    'GiamPierre Huamán' ]
    return render(request,'index.html',{
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango (Desde el View)',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo': 'Saludo',
        'autor_saludo': 'Mg. Flor Elizabeth Cerdán León' 
    })

def rango(request):
   a = 10
   b = 20
   rango_numeros = range(a,b+1)
   return render(request,'rango.html',{
        'titulo': 'Rango',
        'a': a,
        'b': b,
        'rango_numeros': rango_numeros 
    })

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)

    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)