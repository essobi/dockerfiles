FROM java:8-jdk  
MAINTAINER mwio  
  
# In case someone loses the Dockerfile  
RUN rm -rf /etc/Dockerfile  
ADD Dockerfile /etc/Dockerfile  
  
# Install Grails  
ENV GRAILS_VERSION 3.1.7  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v${GRAILS_VERSION}/grails-${GRAILS_VERSION}.zip && \  
unzip grails-${GRAILS_VERSION}.zip && \  
rm -rf grails-${GRAILS_VERSION}.zip && \  
ln -s grails-${GRAILS_VERSION} grails  
  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Create App Directory  
RUN mkdir /app  
WORKDIR /app  
  
# Set Default Behavior  
ENTRYPOINT ["grails"]  
CMD ["-version"]

