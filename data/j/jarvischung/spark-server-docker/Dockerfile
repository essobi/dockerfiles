# Base image to ubuntu:14.04  
FROM ubuntu:14.04  
# Author Jarvis  
MAINTAINER Jarvis  
  
RUN apt-get -qq update  
RUN apt-get -qqy install vim nodejs npm git wget unzip  
  
# link nodejs to node  
RUN ln -s `which nodejs` /usr/bin/node  
  
# Download Spark-Server  
RUN git clone https://github.com/spark/spark-server.git  
RUN cd /spark-server && npm install  
  
# Upgrade Spark-Protocol  
RUN cd /spark-server && npm uninstall spark-protocol  
RUN cd /spark-server && wget "https://github.com/mfferreira/spark-
protocol/archive/master.zip"  
RUN cd /spark-server && unzip master.zip && rm master.zip  
RUN cd /spark-server && npm install ./spark-protocol-master/  
  
# Install Particle-cli and js lib  
RUN npm install -g particle-cli  
RUN npm install -g particle-api-js  
  
# Add run script  
ADD run_spark.sh ./  
  
# Run Spark-Server  
# RUN ./run_spark.sh  
# /bin/sh -c "/run_spark.sh"  
ENTRYPOINT ["/bin/sh","-c","/run_spark.sh",">>","/var/log/spark.log"]  

