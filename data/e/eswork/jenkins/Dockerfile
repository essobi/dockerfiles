FROM jenkins/jenkins:lts  
LABEL maintainer "v.la@live.cn"  
  
USER root  
  
ARG BUILD_CHINA=false  
  
COPY install.sh /usr/src/install.sh  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
RUN bash /usr/src/install.sh  
  
USER jenkins  
  
COPY plugins.txt /usr/share/jenkins/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

