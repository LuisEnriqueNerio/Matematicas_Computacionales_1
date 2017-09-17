dir = "C:/Users/Luis Nerio/Desktop/Academico/Matematicas Computacionales"
setwd(dir)
datos = read.csv("datosg.csv")
library("ggplot2")
#8C2318
#CF4647
r= ggplot(datos) +geom_point(aes(x=length, y=bubble),colour = "#8C2318", alpha=.5) + geom_smooth(aes(x=length, y=bubble,colour="Burbuja"), size = .7) + geom_point(aes(x=length, y=selection), colour ="#0D6759", alpha=.5) + geom_smooth(aes(x=length, y=selection,colour ="Selection"), size = .7) + geom_point(aes(x=length, y=insertion), colour="#EDC951", alpha = .5) + geom_smooth(aes(x=length, y=insertion,colour ="Insertion"), size = .7 )+ geom_point(aes(x=length, y=quick),colour = "#91204D", alpha = .5) + geom_smooth(aes(x=length, y=quick,colour = "Quicksort"), size = .7)+ scale_color_manual("Tipo ordenamiento" ,breaks =c("Burbuja", "Selection", "Insertion", "Quicksort"), values = c("#8C2318","#EDC951","#91204D","#0D6759")  )+xlab("Longitud del arreglo")+ylab("O(longitud arreglo)")+ labs(title= "Complejidad computacional de diferentes tipos de algoritmos de ordenamiento")
###91204D #0D6759

b = ggplot(datos) + geom_boxplot(aes(x=factor(length), y = bubble,colour="Burbuja"))+scale_color_manual("Tipo ordenamiento" ,breaks ="Burbuja", values ="#8C2318" )+ xlab("longitud del arreglo")+ ylab("O(longitud arreglo)")+labs(title= "Diagramas de caja para algoritmo de ordenamiento burbuja")
s = ggplot(datos) + geom_boxplot(aes(x=factor(length), y = selection,colour="Selection"))+scale_color_manual("Tipo ordenamiento" ,breaks ="Selection", values ="#0D6759" )+ xlab("longitud del arreglo")+ ylab("O(longitud arreglo)")+labs(title= "Diagramas de caja para algoritmo de ordenamiento selection")
i = ggplot(datos) + geom_boxplot(aes(x=factor(length), y = insertion,colour="Insertion"))+scale_color_manual("Tipo ordenamiento" ,breaks ="Insertion", values ="#EDC951" )+ xlab("longitud del arreglo")+ ylab("O(longitud arreglo)")+labs(title= "Diagramas de caja para algoritmo de ordenamiento Insertion")
q = ggplot(datos) + geom_boxplot(aes(x=factor(length), y = quick,colour="Quicksort"))+scale_color_manual("Tipo ordenamiento" ,breaks ="Quicksort", values ="#91204D" )+ xlab("longitud del arreglo")+ ylab("O(longitud arreglo)")+labs(title= "Diagramas de caja para algoritmo de ordenamiento Quicksort")

