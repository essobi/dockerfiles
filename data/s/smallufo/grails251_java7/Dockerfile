FROM smallufo/java7  
MAINTAINER smallufo smallufo@gmail.com  
  
USER smallufo  
WORKDIR /home/smallufo  
  
ENV GRAILS_VERSION 2.5.1  
RUN wget https://github.com/grails/grails-
core/releases/download/v${GRAILS_VERSION}/grails-${GRAILS_VERSION}.zip && \  
unzip grails-${GRAILS_VERSION}.zip && \  
rm -rf grails-${GRAILS_VERSION}.zip && \  
ln -s grails-${GRAILS_VERSION} grails  
  
ENV GRAILS_HOME /home/smallufo/grails-${GRAILS_VERSION}  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Create App Directory  
RUN mkdir app  
WORKDIR app  
  
# Set Default Behavior  
#ENTRYPOINT ["grails"]  
#CMD ["-version"]  

