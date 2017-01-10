from xml.dom import minidom
from builtins import int

doc = minidom.parse("fichero.xml")

totalCosteTrabajadores = 0;

listaempleados = doc.getElementsByTagName("trabajadores")
for empleado in listaempleados:
        costeportrabajador = empleado.getElementsByTagName("costeportrabajador")[0]
        coste = int(costeportrabajador.firstChild.data);
        numtrabajadores = empleado.getElementsByTagName("numtrabajadores")[0]
        trabajadores = int(numtrabajadores.firstChild.data);
        
        costeTotal = coste * trabajadores;
        
        totalCosteTrabajadores = totalCosteTrabajadores + costeTotal;
        
print("El coste total de todos los trabajadores es: ", totalCosteTrabajadores);