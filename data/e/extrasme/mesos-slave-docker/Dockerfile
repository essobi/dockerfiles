FROM extrasme/mesos  
MAINTAINER tech@extrasme.com  
  
RUN apt-get update && apt-get install -y apt-transport-https  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update && apt-get install -y docker-engine=1.7.1* && apt-get clean  
  
ENV MESOS_EXECUTOR_REGISTRATION_TIMEOUT=5mins
MESOS_CONTAINERIZERS=docker,mesos MESOS_LAUNCHER=posix  
  
COPY *.sh /mesos/  
RUN chmod +x *.sh  
  
ENTRYPOINT ["./start.sh"]  

