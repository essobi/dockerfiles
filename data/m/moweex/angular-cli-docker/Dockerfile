FROM node:6.9  
  
ENV NG_CLI=@angular/cli  
ENV WEBPACK=webpack  
ENV TS=typescript  
  
RUN apt-get update  
RUN apt-get install gzip  
RUN apt-get -y install rsync  
RUN apt-get install sshpass  
RUN npm install $NG_CLI $WEBPACK $TS -g  

