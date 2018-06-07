# CC-Gesco-DatabaseManagement 1.0  
FROM ubuntu:15.10  
MAINTAINER German Martinez <germaaan@gmail.com> Version: 1.0  
# Instalar Git y Node.js  
RUN apt-get update  
RUN apt-get -y install wget net-tools  
RUN wget -qO- https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y git nodejs  
  
# Clonar el repositorio de la aplicación  
RUN git clone https://github.com/Gescosolution/Gesco-DatabaseManagement.git
/home/Gesco-DatabaseManagement  
WORKDIR "/home/Gesco-DatabaseManagement"  
  
# Desplegar la aplicación  
RUN npm -g install gulp bower  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 5000  
RUN ifconfig eth0  
CMD ["gulp", "server"]  

