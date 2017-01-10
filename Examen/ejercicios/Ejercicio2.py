from xml.dom import minidom
from builtins import int

doc = minidom.parse("fichero.xml")

costeMaximo = 0;


costeportrabajador = 0;

listaempleados = doc.getElementsByTagName("trabajadores")
for empleado in listaempleados:
        costeportrabajador = empleado.getElementsByTagName("costeportrabajador")[0]
        costeportrabajador = int(costeportrabajador.firstChild.data)
        
        
costeMinimo = costeportrabajador;



listaempleados = doc.getElementsByTagName("trabajadores")
for empleado in listaempleados:
        costeportrabajador = empleado.getElementsByTagName("costeportrabajador")[0]
        coste = int(costeportrabajador.firstChild.data);
        
        if coste < costeMinimo:
            costeMinimo = coste;
        if coste > costeMaximo:
            costeMaximo = coste;
        
print("Salario minimo: ", costeMinimo);
print("Salario maximo: ", costeMaximo);
