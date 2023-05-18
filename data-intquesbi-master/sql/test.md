## SQL

Supongamos que tenemos el siguiente esquema de Base de Datos

* Policies
* status podrá ser activa o inactiva
* Claims
* claim_type podrá ser telemático, presencial o mixto
* Users

<img src="E-R test.png" />

Escribe en SQL para extraer la siguente información

**1)** Número de pólizas activas

<br/>


**2)** Listado de todas las campañías activas. Una compañia está activa si al menos hay una poliza activa (company_id)

<br/>

**3)** Número de compañías activas

<br/>

**4)** Numero de siniestros por cada poliza desglosado por tipo de siniestro

<img src="Q4.png" />

<br/>

**5)** Número de siniestros por compañía y por tipo de evento

<img src="Q5.png" />

<br/>

**6)** ¿Cómo crearias la tabla para relacionar usuarios y polizas?

**7)** Número de polizas por usuario y por estado de la poliza teniendo en cuenta que puedes usar la tabla de la relación anterior
