FROM debian:8  
MAINTAINER Camille Meulien <cmeulien@heliostech.fr>  
  
RUN apt-get update \  
&& apt-get install -y postfix mailutils rsyslog curl  
  
RUN curl https://www.kaigara.org/get | sh  
  
COPY ./operations/ /opt/kaigara/operations/  
COPY ./resources/ /etc/kaigara/resources/  
  
COPY bin/entrypoint.sh /usr/bin/  
RUN chmod 755 /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
EXPOSE 25  

