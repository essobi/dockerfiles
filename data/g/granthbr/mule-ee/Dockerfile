FROM java:openjdk-8-jdk  
  
# FROM openjdk:alpine  
# 3.8.3 ee branch  
MAINTAINER Brandon Grantham <brandon.grantham@mulesoft.com>  
  
WORKDIR /opt  
RUN useradd --user-group --shell /bin/false mule && chown mule /opt  
USER mule  
RUN wget https://s3.amazonaws.com/new-mule-artifacts/mule-ee-distribution-
standalone-3.8.5.zip \  
&& unzip *.zip \  
&& ln -s mule-enterprise-standalone-3.8.5 mule && rm mule-ee-distribution-
standalone-3.8.5.zip  
  
# to add a license insert the following line  
# ADD ./*.lic /opt/mule-enterprise-standalone-3.8.5/conf  
ADD ./start.sh /opt  
# to complete the license install uncomment the next line  
# RUN mule/bin/mule -installLicense mule/conf/mule-ee-license.lic && rm -f
mule/conf/mule-ee-license.lic && rm -Rf examples  
#  
# # Define environment variables.  
ENV MULE_HOME /opt/mule  
#  
# # Define mount points.  
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps",
"/opt/mule/domains"]  
#  
# # Define working directory.  
WORKDIR /opt/mule  
#  
CMD [ "./start.sh" ]  
#  
# # Default http port  
EXPOSE 8081  
EXPOSE 8082  
EXPOSE 8084  
EXPOSE 8085  
EXPOSE 8091  
EXPOSE 8090

