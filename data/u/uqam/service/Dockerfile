FROM ubuntu:14.04.3  
MAINTAINER Gabriel Com <com.gabriel@uqam.ca>  
  
#Installer les outils de base  
RUN apt-get update && apt-get install -y curl vim  
  
#Installer Node 4  
RUN curl -sL http://deb.nodesource.com/setup_4.x | sudo -E bash - &&\  
apt-get install -y nodejs  
  
#Variables d'environnement  
ENV PORT 8080  
#Le répertoire de travail  
RUN mkdir /www  
WORKDIR /www  
  
#Copier les fichiers d'exécution  
COPY ./dist /www  
  
#Installer les paquets de base  
RUN npm install  
  
EXPOSE 8080  
#Démarrer le site  
CMD ["npm", "start"]

