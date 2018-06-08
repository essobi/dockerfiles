  
FROM sitapati/magikcraft-js-dev:latest  
  
MAINTAINER Josh Wulf <josh@magikcraft.io>  
  
# Sinopia Version / Path / Backup  
RUN npm install -g sinopia --no-optional --no-shrinkwrap && \  
npm cache clean  
  
EXPOSE 4873  
ENTRYPOINT ["sinopia", "-l", "0.0.0.0:4873"]  

