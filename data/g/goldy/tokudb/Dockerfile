FROM mariadb:5.5.41  
MAINTAINER Christophe Mehay <cmehay@online.net>  
  
ENV PATH /opt/tokutek/mysql/bin/:${PATH}  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget --no-check-certificate -O /tmp/tokudb.tar.gz
https://s3.amazonaws.com/tokudb-7.5.5/mariadb-5.5.41-tokudb-7.5.5-linux-x86_64.tar.gz  
  
RUN mkdir /opt/tokutek/  
RUN tar -xzvf /tmp/tokudb.tar.gz -C /opt/tokutek/  
RUN mv /opt/tokutek/mariadb-5.5.41-tokudb-7.5.5-linux-x86_64
/opt/tokutek/mysql/  
RUN cp -r /opt/tokutek/mysql/lib/plugin /usr/lib/plugin  
  
ADD docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  

