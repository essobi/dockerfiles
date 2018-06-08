FROM mbentley/oracle-jdk7:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install prereqs  
RUN (apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl
git-core unzip wget)  
  
# install grails  
ENV GRAILS_VER 2.4.2  
RUN (wget
http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-${GRAILS_VER}.zip
-O /opt/grails-${GRAILS_VER}.zip &&\  
cd /opt &&\  
unzip grails-${GRAILS_VER}.zip &&\  
rm grails-${GRAILS_VER}.zip &&\  
update-alternatives --install /opt/grails grails /opt/grails-${GRAILS_VER} 1)  
  
# setup data directory  
RUN mkdir /data  
WORKDIR /data  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV GRAILS_HOME /opt/grails  
ENV PATH $PATH:$GRAILS_HOME/bin  
  
ENTRYPOINT ["grails","--plain-output"]  
CMD ["help"]  

