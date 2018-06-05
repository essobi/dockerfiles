FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install wget  
RUN wget -O /etc/apt/sources.list.d/ambari.list http://public-
repo-1.hortonworks.com/ambari/ubuntu16/2.x/updates/2.6.0.0/ambari.list  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
&& apt-get update  
  
RUN apt-get install -y ambari-agent  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

