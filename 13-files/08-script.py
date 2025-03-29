
js_code = """
console.log("Hola desde un archivo JS generado con Python");
function suma(a,b){
    return a + b;
}
"""

with open("script.js", "w") as file:
    file.write(js_code)
