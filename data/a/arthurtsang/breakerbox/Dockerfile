FROM java:openjdk-7-jre  
  
MAINTAINER Arthur Tsang <chiuwai.tsang@hp.com>  
  
RUN useradd breakerbox  
RUN mkdir -p /home/breakerbox  
RUN chown -R breakerbox:breakerbox /home/breakerbox  
  
USER breakerbox  
  
ADD ./config.properties /home/breakerbox/config.properties  
ADD ./breakerbox.yml /home/breakerbox/breakerbox.yml  
ADD ./breakerbox-service-0.1.5-SNAPSHOT.jar /home/breakerbox/breakerbox-
service-0.1.5-SNAPSHOT.jar  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
EXPOSE 8080 8081  
  
WORKDIR /home/breakerbox  
  
  
CMD java -jar breakerbox-service-0.1.5-SNAPSHOT.jar server breakerbox.yml  

