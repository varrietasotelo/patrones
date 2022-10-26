El objetivo es tener una unica instancia de una clase durante toda la aplicacion, es decir que todos los usuarios utilicen esa instancia. 
permite tener una unica instancia de una clase para ser utilizado durante toda la aplicacion, su desventaja es que no puede ser utilizado durante toda la aplicacion, en algunos momentos se deben crear instancias nuevas. 

![Image text](https://github.com/varrietasotelo/ApiRestFirst/blob/main/image/GetAllStore.png) 
Resuelve el problema de la duplicidad de informacion, existen casos en donde todos los usuarios requieren de la misma informacion, entonces para solucionarlo se crea un unico objeto con esta informacion para que sea instanciado por cada usuario que necesite esta informacion, asi todos utilizan el mismo objeto y se optimiza el consumo de memoria. 

El ejemplo del video es el siguiente: 
![Image text](https://github.com/varrietasotelo/ApiRestFirst/blob/main/image/GetAllStore.png) 
En el lenguaje Java en una clase se crea un objeto de ambito estatico y privado (para evitar crear otras instancias), las diferencias entre Metodos de instancia y Metodos de clase son: 
    
    Metodos de instancia: es el ambito no estatico, solo puede ser accedido por una instancia u objeto de clase. 
    Metodos de clase: metodo static: solo puede referenciar varibales estaticas y puede ser accedido a traves de la definicion de la clase, un ejemplo es el metodo main,     porque al iniciar el programa no hay objetos. 
    
Posteriormente se crea un constructor de ambito privado, para que cuando se quiera crear un objeto no se podra utilizar el operador new, entonce se debe crear un metodo de tipo estatico de tipo get el cual si la instancia es null se va a instanciar, si se llama de nuevo pero ya esta instanciado, simplemente devolveria la instancia ya realizada. 

Prueba del video de que el aplicativo solo instancia una unica vez para la conexion de diferentes usuarios: 
![Image text](https://github.com/varrietasotelo/ApiRestFirst/blob/main/image/GetAllStore.png) 


    
