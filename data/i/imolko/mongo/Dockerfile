FROM mongo:3.4  
MAINTAINER Yohany Flores <yohanyflores@gmail.com>  
  
LABEL com.imolko.group=imolko  
LABEL com.imolko.type=base  
  
#configuramos la zona horaria  
RUN echo "America/Caracas" > /etc/timezone && dpkg-reconfigure -f
noninteractive tzdata  
  
# Reinstalamos curl, que no fue incluido por la nueva version de mongo.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl \  
numactl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copiamos los scripts para la configuracion de elastic.  
COPY scripts /scripts  
COPY data-sample /data-sample  
  
RUN ln -sf /dev/stdout /var/log/setup-replicaset.log \  
&& ln -sf /dev/stdout /var/log/setup-data-sample.log  
  
EXPOSE 27017 28017  
ENTRYPOINT ["/scripts/imolko-entrypoint.sh"]  
  
CMD ["mongod"]  
  

