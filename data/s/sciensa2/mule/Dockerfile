FROM java:openjdk-8-jdk  
  
RUN apt-get update  
  
RUN apt-get install -y maven  
  
RUN cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.8.1/mule-standalone-3.8.1.tar.gz  
  
RUN cd /opt && tar xvzf ~/mule-standalone-3.8.1.tar.gz && rm ~/mule-
standalone-3.8.1.tar.gz && ln -s /opt/mule-standalone-3.8.1 /opt/mule  
  
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64  
  
# Define environment variables.  
ENV MULE_HOME /opt/mule  
  
# Set the timezone.  
RUN echo "America/Sao_Paulo" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Define mount points.  
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
  
# Define working directory.  
WORKDIR /opt/mule  
  
#Entrypoint  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["su", "-c", "/usr/bin/entrypoint.sh"]  
  
# Default http port  
EXPOSE 8080  

