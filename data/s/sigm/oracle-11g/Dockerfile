# Selección de versión de Oracle a usar  
# https://github.com/wnameless/docker-oracle-xe-11g  
FROM wnameless/oracle-xe-11g:14.04.4  
  
MAINTAINER ignacio.barrancos@carm.es  
  
# Permitir conectar a oracle en remoto  
ENV ORACLE_ALLOW_REMOTE true  
# Instalar paquetes que faltan  
RUN apt-get -qq update && \  
apt-get -q -y upgrade && \  
apt-get install -y unzip wget && \  
rm -rf /var/lib/apt/lists/*  
# Fijar version de SIGM a desplegar  
ENV SIGM_VERSION 3.0.1-M2  
  
# Fijar Repositorio de artefactos  
# Si no se establece habrá que añadir el fichero
sigem_bd_dist-${SIGM_VERSION}-bd.zip  
ENV SIGM_REPO http://casa.tecnoquia.com/SIGM/mvn-repo  
  
# Desplegar scripts de creación de base de datos  
RUN mkdir -p /var/lib/sigm  
ADD assets/deploy.sh /var/lib/sigm/deploy.sh  
## ADD sigem_bd_dist-${SIGM_VERSION}-bd.zip
/var/lib/sigm/sigem_bd_dist-${SIGM_VERSION}-bd.zip  
# Preparación de scripts de bases de datos de SIGM  
RUN chmod a+x /var/lib/sigm/deploy.sh && \  
/var/lib/sigm/deploy.sh  
# Entorno castellando  
ADD assets/set-spanish-lang-debian.sh /bin/set-spanish-lang-debian.sh  
RUN chmod a+x /bin/set-spanish-lang-debian.sh && /bin/set-spanish-lang-
debian.sh  
ENV LANG es_ES@euro  
  
# Variables para Oracle  
ENV NLS_LANG spanish_spain.WE8ISO8859P15  
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe  
ENV SQLPLUS $ORACLE_HOME/bin/sqlplus  
  
# Inicializacion de la base de datos  
ADD assets/initdb.sh /var/lib/sigm/initdb.sh  
RUN chmod a+x /var/lib/sigm/initdb.sh && \  
/var/lib/sigm/initdb.sh && \  
rm -fr /var/lib/sigm  
#  
# Construir con:  
# docker build -t sigm/oracle-11g:3.0.1-M2 .  
#  
# Ejecutar interactivo (y comprobar si falla algo con):  
# docker run -p 1521:1521 -p 49160:22 -d sigm/oracle-11g:3.0.1-M2  
#  

