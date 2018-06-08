FROM java:openjdk-8-jdk  
  
MAINTAINER victor.romero@gmail.com  
  
# Downloads and extracts MuleSoft  
RUN cd ~ && wget https://repository-
master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.9.0/mule-standalone-3.9.0.tar.gz && echo
"39b773bf20702f614faf30b2ffca4716 mule-standalone-3.9.0.tar.gz" | md5sum -c  
  
RUN cd /opt && tar xvzf ~/mule-standalone-3.9.0.tar.gz && rm ~/mule-
standalone-3.9.0.tar.gz && ln -s /opt/mule-standalone-3.9.0 /opt/mule  
  
# Downloads and extracts Maven  
RUN cd ~ && wget http://www-
us.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz
&& echo "948110de4aab290033c23bf4894f7d9a apache-maven-3.5.2-bin.tar.gz" |
md5sum -c  
  
RUN cd /opt && tar -xvzf ~/apache-maven-3.5.2-bin.tar.gz && rm ~/apache-
maven-3.5.2-bin.tar.gz  
  
# Define environment variables.  
ENV MULE_HOME /opt/mule  
  
# Define Maven path  
ENV PATH="/opt/apache-maven-3.5.2/bin:${PATH}"  
# Define mount points.  
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
  
# Define working directory.  
WORKDIR /opt/mule  
  
CMD [ "/opt/mule/bin/mule" ]  
  
# Default http port  
EXPOSE 8081  

