FROM ubuntu:12.04  
MAINTAINER Sergey Pyankov "esergion@gmail.com"  
RUN locale-gen ru_RU.UTF-8  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU:ru  
ENV LC_ALL ru_RU.UTF-8  
ENV LC_COLLATE ru_RU.UTF-8  
RUN LC_ALL=ru_RU.UTF-8 LC_COLLATE=ru_RU.UTF-8 DEBIAN_FRONTEND=noninteractive \  
echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d && \  
apt-get update && \  
apt-get install -y -q postgresql-9.1 postgresql-contrib-9.1 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
RUN pg_dropcluster --stop 9.1 main  
RUN pg_createcluster --locale ru_RU.UTF-8 9.1 main  
RUN rm /usr/sbin/policy-rc.d && \  
echo 'host all all 0.0.0.0/0 md5' >> /etc/postgresql/9.1/main/pg_hba.conf && \  
sed -i -e"s/var\/lib/opt/g" /etc/postgresql/9.1/main/postgresql.conf  
  
ADD . /usr/bin  
RUN chmod +x /usr/bin/start_pgsql.sh  
  
EXPOSE 5432  

