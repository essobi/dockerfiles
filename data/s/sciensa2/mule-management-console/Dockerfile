FROM java:openjdk-8-jdk  
  
MAINTAINER rafael.bueno@soaexpert.com.br  
  
RUN cd ~ && wget http://mulesoft-training.com/mule-runtime-bundle-3.7.zip &&
echo "9c9731b86b57eac4431192fbc17d6ce6 mule-runtime-bundle-3.7.zip" | md5sum
-c  
  
RUN cd /opt && unzip -a ~/mule-runtime-bundle-3.7.zip && rm ~/mule-runtime-
bundle-3.7.zip && ln -s /opt/mule-runtime-bundle-3.7 /opt/mule  
  
# Define environment variables.  
ENV MMC_HOME /opt/mule/mmc-3.7.0/apache-tomcat-7.0.52  
# Define mount points.  
VOLUME ["/opt/mule/mmc-3.7.0/apache-tomcat-7.0.52/logs",
"/opt/mule/mmc-3.7.0/apache-tomcat-7.0.52/conf", "/opt/mule/mmc-3.7.0/apache-
tomcat-7.0.52/webapps", "/opt/mule/mmc-3.7.0/apache-tomcat-7.0.52/mmc-data"]  
  
# Define working directory.  
WORKDIR /opt/mule/mmc-3.7.0  
  
# Run and expose the ports from Mule Management Console  
EXPOSE 8585  
#CMD nohup /opt/mule/mmc-3.7.0/apache-tomcat-7.0.52/bin/startup.sh &  
#gambeta  
RUN touch file.log  
CMD tail -f file.log  
  

