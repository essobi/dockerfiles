FROM dockerfile/java:oracle-java7  
MAINTAINER Martin Chalupa <chalimartines@gmail.com>  
  
#Base image doesn't start in root  
WORKDIR /  
  
RUN wget -qO - http://packages.confluent.io/deb/1.0/archive.key | sudo apt-key
add -  
RUN sudo add-apt-repository "deb [arch=all]
http://packages.confluent.io/deb/1.0 stable main"  
RUN sudo apt-get update && sudo apt-get install -y confluent-platform-2.11.5  
  
COPY start-platform.sh /usr/bin/start-platform.sh  
RUN chmod +x /usr/bin/start-platform.sh  
  
EXPOSE 2181 9092 8081 8082  
CMD ["/usr/bin/start-platform.sh"]

