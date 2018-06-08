FROM java:8  
MAINTAINER Adi Pellumbi <adi.pellumbi@explorite.com>  
  
# Install Grails  
ENV GRAILS_VERSION 3.2.8  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Download python3  
RUN apt-get update  
RUN apt-get install -y python-pip  
RUN apt-get install -y python3  
RUN pip install boto3==1.3.0  
  
# Create App Directory  
RUN mkdir /app  
  
# Set Workdir  
WORKDIR /app  
  
# Set Default Behavior  
ENTRYPOINT ["grails"]  

