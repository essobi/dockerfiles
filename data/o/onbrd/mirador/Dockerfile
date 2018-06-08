FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y nodejs npm && apt-get install nodejs-
legacy && apt-get install -y git  
  
RUN npm config set registry http://registry.npmjs.org/  
  
RUN npm install -g grunt-cli && npm install -g bower  
  
RUN git clone https://github.com/ProjectMirador/mirador.git  
  
RUN cd mirador && npm install  
RUN cd mirador && bower --allow-root install  
RUN cd mirador && grunt  
  
CMD cd mirador && grunt serve

