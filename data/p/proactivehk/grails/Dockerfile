# Credits:  
# https://github.com/mozart-analytics/grails-docker  
FROM openjdk:8  
# Set customizable env vars defaults.  
# Set Grails version  
ENV GRAILS_VERSION 3.3.1  
# Install Grails  
WORKDIR /opt  
  
# TODO put grails zips on your own server with decent bandwidth  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /opt/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Create App Directory  
RUN mkdir /app  
  
# Set Workdir  
WORKDIR /app  
  
# # Define default command.  
# CMD ["bash"]

