FROM ubuntu:trusty  
  
MAINTAINER lanzx  
  
ADD sources.list /etc/apt/  
  
WORKDIR /  
  
RUN apt-get update  
RUN apt-get install curl -y  
RUN apt-get install wget -y  
RUN apt-get install xz-utils -y  
RUN echo 'install complated'  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
# ENTRYPOINT ["/entrypoint.sh", "/bin/bash"]  
CMD /bin/bash  
  
EXPOSE 8888  

