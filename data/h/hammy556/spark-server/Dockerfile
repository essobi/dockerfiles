# Base image  
FROM phusion/baseimage:0.9.19  
# Author  
MAINTAINER Hammy223  
  
# ports and volumes  
EXPOSE 8080  
VOLUME ["/config"]  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get -qq update  
RUN apt-get -qqy install vim nodejs npm git wget unzip  
  
# link nodejs to node  
RUN ln -s `which nodejs` /usr/bin/node  
  
RUN mkdir -p /etc/my_init.d && \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Download Spark-Server  
#RUN git clone https://github.com/spark/spark-server.git  
#RUN cd /spark-server && npm install  
# Upgrade Spark-Protocol  
#RUN cd /spark-server && npm uninstall spark-protocol  
#RUN cd /spark-server && wget "https://github.com/mfferreira/spark-
protocol/archive/master.zip"  
#RUN cd /spark-server && unzip master.zip && rm master.zip  
#RUN cd /spark-server && npm install ./spark-protocol-master/  
# Install Particle-cli and js lib  
#RUN npm install -g particle-cli  
#RUN npm install -g particle-api-js  
# Clean up APT when done.  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#RUN ls -s /config /spark-server  
# Add run script  
#ADD run_spark.sh ./  
# Run Spark-Server  
# RUN ./run_spark.sh  
# /bin/sh -c "/run_spark.sh"  
ENTRYPOINT ["/bin/sh","-c","/run_spark.sh",">>","/var/log/spark.log"]  
  

