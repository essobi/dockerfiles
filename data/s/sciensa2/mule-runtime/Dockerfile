FROM java:openjdk-8-jdk  
  
MAINTAINER rafael.bueno@soaexpert.com.br  
  
RUN cd ~ && wget http://mulesoft-training.com/mule-runtime-bundle-3.7.zip &&
echo "9c9731b86b57eac4431192fbc17d6ce6 mule-runtime-bundle-3.7.zip" | md5sum
-c  
  
RUN cd /opt && unzip -a ~/mule-runtime-bundle-3.7.zip && rm ~/mule-runtime-
bundle-3.7.zip && ln -s /opt/mule-runtime-bundle-3.7 /opt/mule  
  
# Define environment variables.  
ENV MULE_HOME /opt/mule/mule-enterprise-standalone-3.7.3  
# Define mount points.  
VOLUME ["/opt/mule/mule-enterprise-standalone-3.7.3/logs", "/opt/mule/mule-
enterprise-standalone-3.7.3/apps", "/opt/mule/mule-enterprise-
standalone-3.7.3/conf"]  
  
# Define working directory.  
WORKDIR /opt/mule/mule-enterprise-standalone-3.7.3  
  
# Run and expose the ports from Mule Runtime  
EXPOSE 7777 8081  
CMD /opt/mule/mule-enterprise-standalone-3.7.3/bin/mule  

