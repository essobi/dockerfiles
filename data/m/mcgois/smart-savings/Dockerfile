FROM node:8.1.0  
MAINTAINER Matheus Cabral <matheus.cabral@gmail.com>  
  
# atualiza container  
RUN apt-get update -y  
  
# Install apt-transport-https for Yarn repository  
RUN apt-get install apt-transport-https -y  
  
# instala o yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -y  
RUN apt-get install yarn -y  
  
# Cria diretorio onde ficara a aplicacao  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# instala dependencias  
COPY package.json /usr/src/app  
RUN yarn install  
  
# copia a aplicacao  
COPY . /usr/src/app  
  
# expose ports (-P option)  
EXPOSE 7777  
# executa o node  
CMD ["yarn", "run", "clean"]  
CMD ["yarn", "run", "build:prod"]  
CMD ["yarn", "run", "prod"]  

