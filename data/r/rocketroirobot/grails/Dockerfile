FROM cogniteev/oracle-java:java8  
  
MAINTAINER Josemy Duarte <josemy.duarte@rocketroi.com>  
  
ENV GRAILS_VERSION 2.5.0  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
RUN apt-get update \  
&& apt-get install -y wget build-essential zip unzip python3-pip python3-dev\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip \  
&& pip install awscli --upgrade --user  
  
ENV PATH="~/.local/bin:${PATH}"  
  
WORKDIR /usr/lib/jvm  
  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
ADD spring-batch /root/.m2/repository/org/grails/plugins/spring-batch  
  
WORKDIR /data  
  
CMD ["grails"]  
  
  

