FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common wget  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
RUN apt-get update && apt-get install -y oracle-java7-installer  
ENV ZK zookeeper:2181  
RUN mkdir -p /helix/helix-admin-webapp  
RUN wget -O /helix/helix-admin-webapp.tar
http://www.carfab.com/apachesoftware/helix/0.6.4/binaries/helix-admin-
webapp-0.6.4-pkg.tar  
RUN tar xf /helix/helix-admin-webapp.tar -C /helix/helix-admin-webapp --strip-
components=1  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV ADMIN_PORT 8100  
CMD cd /helix/helix-admin-webapp/bin && ./run-rest-admin.sh --zkSvr $ZK
\--port $ADMIN_PORT  

