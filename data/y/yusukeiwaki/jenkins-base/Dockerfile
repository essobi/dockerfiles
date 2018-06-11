FROM openjdk:8  
RUN wget https://pkg.jenkins.io/debian/binary/jenkins_1.658_all.deb -O
/tmp/jenkins.deb  
RUN apt-get update && apt-get install -y daemon net-tools apt-utils  
RUN dpkg -i /tmp/jenkins.deb  
  
# change port to 8000  
RUN sed -i -e '/^#.*java.net.pre/s/^#//' /etc/default/jenkins  
RUN sed -i -e 's/HTTP_PORT=8080/HTTP_PORT=8000/' /etc/default/jenkins  
  
EXPOSE 8000  
CMD /etc/init.d/jenkins restart ; /bin/bash  
  

