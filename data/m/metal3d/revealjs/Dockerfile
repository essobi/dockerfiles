FROM node:latest  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
EXPOSE 8000 8001  
ENV THEME black  
ENV SLIDE example.md  
ENV HIGHLIGHT zenburn  
ENV TITLE "Example slide"  
ENV AUTHOR ""  
ENV DESCRIPTION "An example slide"  
ENV USE_REMOTE false  
ENV SEPARATOR "\n---\n"  
ENV VERTICAL_SEPARATOR "\n----\n"  
ENV NOTE "^Note:"  
ENV TRANSITION slide  
  
COPY reveal.js /revealjs  
WORKDIR /revealjs  
  
RUN set -xe;\  
sed -i 's/"node-sass": ".*"/"node-sass": "~3.3"/' package.json;\  
sed -i 's/"grunt-sass": ".*"/"grunt-sass": "~1.0"/' package.json;\  
npm install -g grunt-cli;\  
npm install;\  
npm cache clean  
  
COPY slides /revealjs/slides  
COPY index.html /revealjs/index.html  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  
CMD ["grunt", "serve"]  

