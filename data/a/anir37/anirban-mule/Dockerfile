FROM java:openjdk-8-jdk  
MAINTAINER Anirban Sen Chowdhary, senchowdhary.anirban@gmail.com  
  
# Define environment variables  
ENV MULE_HOME /mule  
  
# Download and install Mule runtime  
WORKDIR /Mule  
CMD echo "------ Unzipping the added zip --------"  
RUN wget https://dl.dropboxusercontent.com/s/0oyk3litr1bobmh/mule-ee-
distribution-standalone-3.8.5.zip && \  
unzip mule-ee-distribution-standalone-3.8.5.zip && \  
rm mule-ee-distribution-standalone-3.8.5.zip && \  
ln -s /Mule/mule-enterprise-standalone-3.8.5 /mule  
  
# Define mount points  
VOLUME ["/mule/logs", "/mule/domains","/mule/bin","/mule/conf"]  
  
#-------------------------------------------------------------------  
# Copy and install license  
#CMD echo "------ Copy and install license --------"  
#COPY ./Licence/mule-ee-license.lic /mule/conf/  
#RUN /mule/bin/mule -installLicense /mule/conf/mule-ee-license.lic  
#Check if Mule Licence installed  
#RUN ls -ltr mule-enterprise-standalone-3.8.5/conf/  
#CMD echo "------ Licence installed ! --------"  
#-------------------------------------------------------------------  
CMD echo "------ Copy and deploy mule application in runtime --------"  
#Copy and deploy mule application in runtime  
CMD echo "------ Deploying mule application in runtime ! --------"  
ADD https://dl.dropboxusercontent.com/s/h0xwffhk4yzb6au/TestApplication.zip .  
#COPY ./TestMuleApp/TestApplication.zip .  
RUN chmod 777 TestApplication.zip  
RUN ls -ltr  
RUN cp TestApplication.zip /mule/apps  
RUN rm TestApplication.zip  
#COPY ./TestMuleApp/TestApplication.zip /mule/apps  
RUN chmod 777 /mule/apps  
RUN ls -ltr /mule/apps  
  
# HTTP Service Port  
# Expose the necessary port ranges as required by the Mule Apps  
EXPOSE 8081-8082  
EXPOSE 9082  
# Mule remote debugger  
EXPOSE 5000  
# Mule JMX port (must match Mule config file)  
EXPOSE 1098  
# Mule MMC agent port  
EXPOSE 7777  
# AMC agent port  
EXPOSE 9997  
# Start Mule runtime  
WORKDIR /mule  
CMD ["/mule/bin/mule"]  

