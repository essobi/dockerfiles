# Version: 1  
# Name: grails2.4.3  
FROM yan047/tomcat7  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# In case someone loses the Dockerfile  
RUN rm -rf /etc/Dockerfile  
ADD Dockerfile /etc/Dockerfile  
  
# Install Grails  
WORKDIR /usr/lib/jvm  
RUN wget
http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-2.4.3.zip  
RUN unzip grails-2.4.3.zip  
RUN rm -rf grails-2.4.3.zip  
RUN ln -s grails-2.4.3 grails  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Create App Directory  
WORKDIR /  
RUN mkdir /app  
WORKDIR /app  

