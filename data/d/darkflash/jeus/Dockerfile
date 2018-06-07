FROM ubuntu:14.04.5  
MAINTAINER khs <darkflash76@gmail.com>  
  
USER root  
  
# COPY jeus50-unix-generic.bin /  
ADD resources/jeus5 /root/jeus5  
ADD resources/jdk1.6 /usr/java/jdk1.6  
ADD resources/run.sh /run.sh  
  
ENV JAVA_HOME /usr/java/jdk1.6  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
RUN chown -R root.root /root/jeus5 /usr/java/jdk1.6 && \  
chmod +x /run.sh  
  
ENV JEUS_HOME=/root/jeus5  
ENV PATH
${PATH}:${JEUS_HOME}/bin:${JEUS_HOME}/lib/system:${JEUS_HOME}/webserver/bin  
  
EXPOSE 9744  
CMD ["/run.sh"]  

