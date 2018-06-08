FROM java:7  
MAINTAINER Eduardo Cuomo <eduardo.cuomo@patagonian.it>  
  
ARG GRAILS_VERSION=2.5.5  
# Install Grails  
WORKDIR /usr/lib/jvm  
  
ADD https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip
/usr/lib/jvm/grails-$GRAILS_VERSION.zip  
RUN unzip grails-$GRAILS_VERSION.zip  
RUN rm -rf grails-$GRAILS_VERSION.zip  
RUN ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Create App Directory  
RUN mkdir /app  
  
# Set Workdir  
WORKDIR /app  
  
# Set Default Behavior  
ENTRYPOINT ["grails"]  

