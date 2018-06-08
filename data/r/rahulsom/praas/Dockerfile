FROM rahulsom/docker-java:7u55  
MAINTAINER Rahul Somasunderam  
  
RUN yum install -y tar unzip  
  
WORKDIR /opt  
  
ADD launch.sh /opt/  
  
RUN source ~/.bashrc && \  
wget -q --no-check-certificate
https://github.com/rahulsom/praas/archive/master.tar.gz && \  
tar xzvf master.tar.gz && \  
rm master.tar.gz  
  
EXPOSE 8080  
ENTRYPOINT /opt/launch.sh  

