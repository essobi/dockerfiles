# Base image and maintainer details  
FROM java:8-jre  
MAINTAINER Enterprise AppsMaker masterCraft.support@tcs.com  
USER root  
COPY EnrollmentComponent-1.0.jar /  
# Expose the http, database and administration ports  
EXPOSE 8761 9990  
# Specify container startup command  
CMD java -jar /EnrollmentComponent-1.0.jar

