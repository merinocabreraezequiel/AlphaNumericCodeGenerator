# ORGIEN
> Para un `Refactor` de un proyecto son surgió una problema. Migrabamos de un sistema por IDs a uno por Códigos.
> Como queriamos mantener las dos funcionalidades durante un tiempo, debiamos discernir si eran numero o códigos, pero, estos códigos eran alphanumeriocos, así que podía darse el caso de un Codigo que si fuese numerico y nos reventaria la solución.
> Pero, en un código de 12 digitos alphanumericos ¿Cuantos son solo numeros? ¿Vale la pena controlar esos casos?

# PRIMEROS CALCULOS
> Empezamos haciendo un sencillo calculo para saber cuantas combinaciones totales hay, resulta que son muchas **62^12**, esto sale de que, son 62 caracteres, todo el abecedario en mayusculas y minusculas más los 10 numeros, y es 12, porque decidimos que 12 digitos era un buen numero "solo 8 se terminarán muy pronto" dije, ***iluso***.
>> 3.2262668e+21, 3226266762397899821056, 3.2262667623979e+21, las calculadoras mas o menos se ponen de acuerdo
> Y de todos estos, cuantos son solo combinaciones numericas?
>> 1e+12, 1000000000000, 1000000000000, en esto todas estan de acuerdo 10^12 es manejable.
> Recuperando mastes de primaria, el tanto porciento debería ser `((10^12)*100)/(62^12)`
>> 3.0995577e-8, 0.00000003099557704449576, 0, vamos, que si no es 0, como dice una de las calculadoras, casi casi casi

# PRIMERAS CONCLUSIONES
> Resulta que es practicamente absurdo contemplar la opción, así que, si es numerico, damos por sentado que es un ID y si peta, ya hay un `try/catch` que se encarga de ello.

# GENERANDO CÓDIGOS
> Todo esto nos hizo preguntarnos cuanto tardariamos en sacar todas las combinaciones posibles desde `aaaaaaaaaaaa` hasta `999999999999`. La respuetsa fue sencilla, lanza un simple script que lo haga, secuencialmente y contando, en python, que se tadan dos minutos.
> Tras más de una semana generando códigos en una maquina dedicada, y no habiendo llegado aún al digito 10, nos dimos cuenta de que talvez habría que replantearlo...
