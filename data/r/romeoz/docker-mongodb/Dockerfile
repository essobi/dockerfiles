FROM ubuntu:xenial  
MAINTAINER romeOz <serggalka@gmail.com>  
  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update && apt-get install -y locales && locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LANGUAGE=${OS_LOCALE} \  
LC_ALL=${OS_LOCALE}  
  
ENV MONGO_USER=mongodb \  
MONGO_DATA_DIR=/var/lib/mongodb \  
MONGO_LOG_DIR=/var/log/mongodb \  
MONGO_CONFIG=/etc/mongodb/mongod.conf  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \  
&& apt-get update && apt-get install -y sudo \  
&& echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-
org-3.6.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY mongod.conf ${MONGO_CONFIG}  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 27017  
VOLUME ["${MONGO_DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]

