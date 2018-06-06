############################################################  
# Dockerfile to build a Slocker container  
# Based on Debian  
############################################################  
  
# Set the base image  
FROM julienstroheker/slocker  
  
# File Author / Maintainer  
MAINTAINER Julien Stroheker  
  
# Export a global variable with our HOOK  
RUN export
Slack_Hook_Url='https://hooks.slack.com/services/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'  
  
# Copy the configuration JSON inside the container  
COPY app/redirectChannel.json /usr/src/app/redirectChannel.json  
  
# Expose port  
EXPOSE 8080  
  
# Set the default command to execute  
# when creating a new container  
# lunch the webserver  
CMD python2 /usr/src/app/slocker.py

