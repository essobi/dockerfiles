# multilevel  
#  
# VERSION: see `TAG`  
FROM joaodubas/nodejs:latest  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install leveldb  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install libleveldb-dev libleveldb1  
  
# provision application  
ENV NODE_PORT 3001  
ENV NODE_DB_PATH /opt/data  
ADD ./app /opt/app  
RUN cd /opt/app \  
&& /usr/local/bin/npm install  
  
# configure execution  
EXPOSE 3001  
WORKDIR /opt/app  
VOLUME ["/opt/data"]  
CMD ["/usr/local/bin/node", "/opt/app/index"]  

