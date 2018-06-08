#  
# Grails legacy docker with java8  
#  
FROM java:8  
MAINTAINER Mike Winkelmann <mikedotwinkelmann@gmail.com>  
  
# legacy version  
ENV GRAILS_VERSION 2.4.5  
# install Grails  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip  
RUN unzip grails-$GRAILS_VERSION.zip  
RUN rm -rf grails-$GRAILS_VERSION.zip  
RUN ln -s grails-$GRAILS_VERSION grails  
  
# setup grails binary to PATH  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $PATH:$GRAILS_HOME/bin  
  
# setup python  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
# create application dir  
RUN mkdir /app  
  
# workdir  
WORKDIR /app  
  
# default entrypoint  
ENTRYPOINT ["grails",] # @args will be appended  
CMD ["help"]  

