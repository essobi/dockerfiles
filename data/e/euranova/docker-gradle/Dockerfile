# Use this image as a base  
FROM frekele/gradle:3.5-jdk8  
MAINTAINER EURA NOVA <info@euranova.eu>  
  
# In case someone loses the Dockerfile  
RUN rm -rf /etc/Dockerfile  
ADD Dockerfile /etc/Dockerfile  
  
ENV GRADLE_USER_HOME /usr/bin/app/.gradle  
WORKDIR /usr/bin/app  
  
# Set the default entrypoint  
ENTRYPOINT ["gradle"]  
  
# Set the default command  
CMD ["assembly", "check"]  
  

