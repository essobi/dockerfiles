#  
# Alpine Glances Dockerfile  
# From https://github.com/nicolargo/glances  
#  
# Modifié et basé sur Alpine  
#  
# Utilisation de l'image Alpine en version stable  
FROM alpine  
  
# Installation des prérequis Python  
RUN apk add --no-cache py2-pip py2-psutil  
  
# Mise à jour de PIP  
RUN pip install --upgrade pip  
  
# Installation de Glances  
RUN pip install glances  
  
# Installation des librairies  
RUN pip install bottle  
RUN pip install pystache  
RUN pip install docker  
RUN pip install py-cpuinfo  
  
#RUN pip install scandir  
#RUN pip install netifaces  
#RUN pip install zeroconf  
#RUN pip install pysnmp  
#RUN pip install py3sensors  
# Define working directory.  
WORKDIR /glances  
  
# EXPOSE PORT (For XMLRPC)  
EXPOSE 61209  
# EXPOSE PORT (For Web UI)  
EXPOSE 61208  
# Define default command.  
CMD python -m glances -C /glances/conf/glances.conf $GLANCES_OPT  

