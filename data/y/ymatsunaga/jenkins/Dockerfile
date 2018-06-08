FROM jenkins:2.7.2  
  
USER root  
  
# setup sudo  
RUN apt-get update \  
&& apt-get install -y sudo \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# setup docker  
#RUN echo "deb http://http.debian.net/debian wheezy-backports main" >
/etc/apt/sources.list.d/backports.list  
#RUN apt-get update && apt-get install -y apt-transport-https ca-certificates  
#RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
#RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
#RUN apt-get update && apt-get install -y docker-engine && rm -rf
/var/lib/apt/lists/*  
  
USER jenkins  
  

