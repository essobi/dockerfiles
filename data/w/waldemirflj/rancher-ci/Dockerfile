# Imagem  
FROM node:8.2.0-alpine  
  
# EU ...  
MAINTAINER Waldemir Francisco <waldemirflj@gmail.com>  
  
# Cria o diretório da app  
RUN mkdir -p /usr/src/app  
  
# Defini o de tranalho da app  
WORKDIR /usr/src/app  
  
# Cópia arquivos necessários  
COPY . /usr/src/app  
  
# Instala dependências  
RUN npm install \  
&& npm cache clean -f  
  
VOLUME /usr/src/app  
  
# Expõe porta interna  
EXPOSE 3000  
# RUN RUN RUNNNN  
CMD ["npm", "start"]  

