# BUILD-WITH sudo docker.io build -t khipu/cargo .  
# RUN-WITH sudo docker.io run -d -h cargo1 --name cargo1 khipu/cargo  
FROM khipu/java8:latest  
MAINTAINER developers@khipu.com  
  
RUN mkdir -p /opt/khipu/cargo && \  
mkdir -p /home/payment/logs && \  
touch /home/payment/logs/empty.txt && \  
chown -R khipu /home/payment/logs /opt/khipu/cargo  
  
USER khipu  
  
WORKDIR /opt/khipu/cargo  
  
RUN curl http://repo1.maven.org/maven2/org/codehaus/cargo/cargo-daemon-
webapp/1.4.14/cargo-daemon-webapp-1.4.14.war -o "cargo-daemon-
webapp-1.4.14.war"  
  
VOLUME ["/opt/khipu/cargo", "/home/payment/logs"]  
  
CMD ["java", "-Ddaemon.home=/opt/khipu/cargo", "-jar", "cargo-daemon-
webapp-1.4.14.war"]  

