#OS  
FROM ubuntu:latest  
  
#Autor/Author  
MAINTAINER Fernando Llodra Belda <llodrab@gmail.com>  
  
#Actualizar sistema/Update System  
RUN sudo apt-get -y update  
  
#Instalar git y descargar app/ Install git and download app  
RUN sudo apt-get install -y git  
RUN git clone https://github.com/Gescosolution/GescoChat.git  
  
# Install Node.js and npm  
RUN sudo apt-get install -y nodejs npm  
  
#Instalar las dependencias de la app/Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install  
  
#Aplicación/Bundle app source  
COPY . /src  
  
EXPOSE 8000  
CMD ["node", "/src/index.js"]

