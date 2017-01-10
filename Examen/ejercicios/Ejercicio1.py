from xml.dom import minidom
from builtins import int

doc = minidom.parse("fichero.xml")

totalTrabajadores = 0;

listaempleados = doc.getElementsByTagName("trabajadores")
for empleado in listaempleados:
        numtrabajadores = empleado.getElementsByTagName("numtrabajadores")[0]
        totalTrabajadores = totalTrabajadores + int(numtrabajadores.firstChild.data);
print("El número de trabajadores es: ", totalTrabajadores);