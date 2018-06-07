FROM docker.io/cassandra:3.7  
  
# Update to latest packages  
RUN apt-get update \  
&& apt-get upgrade -y  
  
RUN sed -i "s/#-Xms4G/-Xms4G/g" /etc/cassandra/jvm.options \  
&& sed -i "s/#-Xmx4G/-Xmx4G/g" /etc/cassandra/jvm.options  

