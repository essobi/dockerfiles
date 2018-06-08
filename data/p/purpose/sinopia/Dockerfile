FROM purpose/sinopia-base  
MAINTAINER Purpose Industries <dev@purposeindustries.co>  
RUN apt-get update && \  
apt-get install --yes --force-yes curl build-essential && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install --yes --force-yes nodejs && \  
npm i -g sinopia  
USER sinopia  
WORKDIR /opt/  
EXPOSE 4873  
CMD sinopia  

