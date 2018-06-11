FROM sergeyzh/centos6-java  
  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN yum install -y unzip  
  
RUN useradd -m buildagent  
  
#container start script  
ADD run-services.sh /run-services.sh  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  
  
EXPOSE 9090  

