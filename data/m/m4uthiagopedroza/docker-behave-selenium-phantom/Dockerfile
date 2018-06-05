FROM ubuntu:14.04  
#Atualizado  
RUN apt-get update  
  
#Instalando Pip  
RUN apt-get -y install python-setuptools python-dev build-essential
libfontconfig  
RUN easy_install pip  
  
#Instalando Node  
RUN apt-get -y install nodejs  
  
#Configurando nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
#Instalando Configurando nodejs-legacy  
RUN apt-get -y install nodejs-legacy  
  
#Instalando NPM  
RUN apt-get -y install npm  
  
#Instalando PhantamJS  
RUN npm install -g phantomjs-prebuilt  
RUN npm install -g phantomjs  
  
#Instalando Chromium  
RUN apt-get install -y chromium-browser  
  
COPY ./requirements.txt /home/requirements.txt  
RUN pip install -r /home/requirements.txt  

