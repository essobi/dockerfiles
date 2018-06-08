FROM errordeveloper/oracle-jre  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
ENV KIBANA_VERSION 4.0.0-BETA3  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/Go_Daddy_Class_2_CA.crt \  
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}.tar.gz
\  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s /usr/kibana-$KIBANA_VERSION /usr/kibana  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 5601  
ENTRYPOINT ["/run.sh"]  

