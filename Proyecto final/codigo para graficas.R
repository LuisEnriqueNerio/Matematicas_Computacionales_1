dir = "C:/Users/Luis Nerio/Desktop/Academico/Matematicas Computacionales/projecto final "
setwd(dir)
datos = read.csv("datos.csv")
library("ggplot2")
#8C2318
#CF4647
r= ggplot(datos) +geom_point(aes(x=Longitud, y=Tiempo1),colour = "#8C2318", alpha=.5)+geom_smooth(aes(x=Longitud, y=Tiempo1,colour="Tiempo1"), size = .7)+geom_point(aes(x=Longitud, y=Tiempo2),colour = "#0D6759", alpha=.5) + geom_smooth(aes(x=Longitud, y=Tiempo2,colour="Tiempo2"), size = .7)
b = ggplot(datos) + geom_boxplot(aes(x=factor(Longitud), y = Tiempo1,colour="T"))+scale_color_manual("Algoritmo" ,breaks ="Mediana normal", values ="#8C2318" )+ xlab("longitud del arreglo")+ ylab("Tiempo")+labs(title= "Diagramas de caja para algoritmo de mediana usual")
c = ggplot(datos) + geom_boxplot(aes(x=factor(Longitud), y = Tiempo2,colour="R"))+scale_color_manual("Algoritmo" ,breaks ="Mediana eficiente", values ="#0D6759" )+ xlab("longitud del arreglo")+ ylab("Tiempo")+labs(title= "Diagramas de caja para algoritmo de mediana eficiente")