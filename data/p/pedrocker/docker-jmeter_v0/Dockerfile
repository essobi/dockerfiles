FROM fedora:23  
RUN dnf -y update  
RUN dnf -y install wget  
RUN dnf -y install tar  
RUN dnf -y install java-1.8.0-openjdk.x86_64  
RUN wget http://apache.mediamirrors.org//jmeter/binaries/apache-jmeter-3.1.tgz  
RUN tar -xvzf apache-jmeter-3.1.tgz  
RUN rm -f apache-jmeter-3.1.tgz  
RUN rm -fr /apache-jmeter-3.1/docs  
RUN mkdir results  
  
COPY *.jmx ./  
COPY *.csv ./  
COPY jmeter.sh ./  
  
VOLUME /results  
  
CMD ["bin/bash"]  
# on peut l'enlever pour faire le link entre services
DOCKER_WEB_SERVER_FLASK_SERVICE_HOST

