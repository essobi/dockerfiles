FROM rodrigozc/consul:1.0.2  
LABEL author.name="Rodrigo Zampieri Castilho"  
LABEL author.email="rodrigo.zampieri@gmail.com"  
LABEL repository.url="https://bitbucket.org/rcastilho/mongodb"  
  
ENV APPLICATION_DEFAULT_NAME "mongodb"  
ENV MONGO_DEFAULT_PATH_CONFIG_FILE "/etc/mongod.conf"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends gnupg2 dirmngr \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 \  
&& echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends mongodb-org \  
&& sed -i'' 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
ADD consul-template/1-consul-template.list /etc/consul-template/  
ADD consul/service.ctmpl /etc/consul/  
ADD consul/service.json /etc/consul/  
ADD run/mongod.sh /docker/run/  

