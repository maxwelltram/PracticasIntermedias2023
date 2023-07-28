import io
import os
import numpy as np
import matplotlib.pyplot as plt
import base64
import discord
from discord.ext import commands
from dotenv import load_dotenv
from sympy import sympify, Eq, solve, symbols

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='_', description='Bot que resuelve ecuaciones y grafica funciones matemáticas', intents=intents)

def getLineal(listVal):
    # Creating vectors X and Y
    x = np.arange(-11, 11, 1)

    a = 0
    b = 0

    contador = 1

    if isinstance(listVal, list):
        for valor in listVal:
            if contador == 1:
                a = float(valor)
            elif contador == 2:
                b = float(valor)            
                contador = 1
                break
            contador += 1

    y = a*x + b
    
    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)

    plt.ylabel('EJE Y')
    plt.xlabel('EJE X')
    plt.title('FUNCIÓN LINEAL')
    plt.grid(True)

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')

    img_buf.seek(0)

    return img_buf

def getCuadratica(listVal):
    # Creating vectors X and Y
    x = np.arange(-11, 11, 1)

    a = 0
    b = 0
    c = 0

    contador = 1

    if isinstance(listVal, list):
        for valor in listVal:
            if contador == 1:
                a = float(valor)
            elif contador == 2:
                b = float(valor)
            elif contador == 3:
                c = float(valor)
                contador = 1
                break
            contador += 1

    y = a*(x**2) + b*x + c
    
    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)

    plt.ylabel('EJE Y')
    plt.xlabel('EJE X')
    plt.title('FUNCIÓN CUADRÁTICA')
    plt.grid(True)

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')

    img_buf.seek(0)

    return img_buf

def getCubica(listVal):
    # Creating vectors X and Y
    x = np.arange(-11, 11, 1)

    a = 0
    b = 0
    c = 0
    d = 0
    contador = 1

    if isinstance(listVal, list):
        for valor in listVal:
            if contador == 1:
                a = float(valor)
            elif contador == 2:
                b = float(valor)
            elif contador == 3:
                c = float(valor)
            elif contador == 4:
                d = float(valor)
                contador = 1
                break
            contador += 1

    y = a*(x**3) + b*(x**2) + c*x + d     
    
    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)

    plt.ylabel('EJE Y')
    plt.xlabel('EJE X')
    plt.title('FUNCIÓN CÚBICA')
    plt.grid(True)

    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')

    img_buf.seek(0)

    return img_buf

def resolverEcuacion(ecuacion):
    x = symbols('x')
    print(ecuacion)
    expresion = sympify(ecuacion)
    eq = Eq(expresion, 0)
    solucion = solve(eq, x)

    return solucion

@bot.command(name='lineal', help='Función que retorna la gráfica de una función lineal')
async def graficaLin(ctx, listValores):
    lista = listValores.split(',')
    img = getLineal(lista)

    data = img.getvalue()
    output = base64.b64encode(data).decode('utf-8')

    file = discord.File(io.BytesIO(base64.b64decode(output)), filename='grafica.png')

    await ctx.send(file = file)  

@bot.command(name='cuadratica', help='Función que retorna la gráfica de una función cuadrática')
async def graficaCuad(ctx, listValores):
    lista = listValores.split(',')
    img = getCuadratica(lista)

    data = img.getvalue()
    output = base64.b64encode(data).decode('utf-8')

    file = discord.File(io.BytesIO(base64.b64decode(output)), filename='grafica.png')

    await ctx.send(file = file)
    

@bot.command(name='cubica', help='Función que retorna la gráfica de una función cúbica')
async def graficaCubi(ctx, listValores):
    lista = listValores.split(',')
    img = getCubica(lista)

    data = img.getvalue()
    output = base64.b64encode(data).decode('utf-8')

    file = discord.File(io.BytesIO(base64.b64decode(output)), filename='grafica.png')

    await ctx.send(file = file)

@bot.command(name='solve', help='Comando que permite resolver una ecuación')
async def ecuacion(ctx, ecuacion):
    data = resolverEcuacion(ecuacion)
    strSolucion = f"La solución de la ecuación {ecuacion} es: {data}"
    await ctx.send(strSolucion)

bot.run(TOKEN)



