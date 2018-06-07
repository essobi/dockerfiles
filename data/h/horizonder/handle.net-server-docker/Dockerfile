FROM openjdk:8u141-jdk  
  
LABEL maintainer="dominic.price@nottingham.ac.uk"  
  
EXPOSE 2461/tcp  
EXPOSE 2461/udp  
EXPOSE 8000/tcp  
  
RUN apt-get update && apt-get install -y --no-install-recommends wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /handle.net-server  
  
WORKDIR /handle.net-server  
  
RUN wget http://www.handle.net/hnr-source/hsj-8.1.4.tar.gz -O hsj.tar.gz \  
&& tar -xf hsj.tar.gz --strip-components=1 \  
&& wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.44.tar.gz \  
&& tar -xf mysql-connector-java-5.1.44.tar.gz -C lib --strip-components=1 \  
mysql-connector-java-5.1.44/mysql-connector-java-5.1.44-bin.jar \  
&& rm mysql-connector-java-5.1.44.tar.gz \  
&& wget https://jdbc.postgresql.org/download/postgresql-42.1.4.jar -P lib  

