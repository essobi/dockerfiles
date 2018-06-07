FROM java:openjdk-8  
#  
# expose the grails default port  
#  
EXPOSE 8080 22  
RUN ln -snf /bin/bash /bin/sh && apt-get update && apt-get install -y redis-
server supervisor git openssh-server && mkdir /data  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY start.sh /data/start.sh  
  
WORKDIR "/data/"  
  
RUN git clone https://github.com/schmalle/ElasticPot.git  
  
WORKDIR "/data/ElasticPot"  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
#  
# this is only needed to download all needed libraries for grails 2.5.3  
#  
RUN ./gradlew war  
  
CMD supervisord  
  

