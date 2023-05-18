/**
Supongamos que tenemos el siguiente esquema de Base de Datos

* Policies
* status podrá ser activa o inactiva
* Claims
* claim_type podrá ser telemático, presencial o mixto
* Users
*/

/**
Escribe en SQL para extraer la siguente información

**1)** Número de pólizas activas


*/

SELECT COUNT(*) as Polizas_activas
FROM Policies
WHERE status = "activa"

/**
**2)** Listado de todas las campañías activas. Una compañia está activa si al menos hay una poliza activa (company_id)

<br/>


*/

SELECT * 
FROM COMPANY
JOIN (SELECT id FROM Policies WHERE status = "activa") AS P ON P.company_id = COMPANY.id

/**
**3)** Número de compañías activas

<br/>
*/

SELECT COUNT(*)
FROM COMPANY
JOIN (SELECT id FROM Policies WHERE status = "activa") AS P ON P.company_id = COMPANY.id

/**
**4)** Numero de siniestros por cada poliza desglosado por tipo de siniestro
*/

SELECT P.NAME AS NOMBRE_POLIZA, COUNT(C.id) AS NumSiniestros
FROM Claims AS C
JOIN POLICIES AS P ON P.ID = C.POLICY_ID
GROUP BY P.NAME 

/**
**5)** Número de siniestros por compañía y por tipo de evento
*/

/**
NO ESTÁ CLARO LA RELACIÓN EN EL DIAGRAMA ENTRE COMPAÑIA, POLIZAS Y SINIESTROS.
*/

/**
**6)** ¿Cómo crearias la tabla para relacionar usuarios y polizas?
*/

CREATE TABLE USUARIOS_POLIZAS(
    ID BIGINT NOT NULL PRIMARY KEY,
    ID_USUARIOS INT NOT NULL,
    ID_POLIZAS INT NOT NULL,
    FOREIGN KEY (ID_USUARIOS) REFERENCES Users(id),
    FOREIGN KEY (ID_POLIZAS) REFERENCES Policies(id)
)

/**
**7)** Número de polizas por usuario y por estado de la poliza teniendo en cuenta que puedes usar la tabla de la relación anterior

*/

SELECT 

COUNT(P.id) AS N_POLIZA,
P.STATUS AS P_STATUS,
U.Name AS U_NAME

FROM Policies P, USERS U
JOIN USUARIOS_POLIZAS AS UP ON UP.ID_POLIZAS = P.id
WHERE U.id = UP.ID_USUARIOS
GROUP BY U.Name, P.STATUS



