FROM clojure:lein-2.8.1  
MAINTAINER publicmayhem ""  
# This is a version of pointslope/datomic-pro-starter with a higher
clojure:lein  
# version to enable docker memory features in final release of java8  
ENV DATOMIC_VERSION 0.9.5561.62  
ENV DATOMIC_HOME /opt/datomic-pro-$DATOMIC_VERSION  
ENV DATOMIC_DATA $DATOMIC_HOME/data  
  
RUN apt-get update  
RUN apt-get install curl unzip  
  
# Datomic Pro Starter as easy as 1-2-3  
# 1. Create a .credentials file containing user:pass  
# for downloading from my.datomic.com  
ONBUILD ADD .credentials /tmp/.credentials  
  
# 2. Make sure to have a config/ folder in the same folder as your  
# Dockerfile containing the transactor property file you wish to use  
ONBUILD RUN curl -u $(cat /tmp/.credentials) -SL
https://my.datomic.com/repo/com/datomic/datomic-pro/$DATOMIC_VERSION/datomic-
pro-$DATOMIC_VERSION.zip -o /tmp/datomic.zip \  
&& unzip /tmp/datomic.zip -d /opt \  
&& rm -f /tmp/datomic.zip  
  
ONBUILD ADD config $DATOMIC_HOME/config  
  
WORKDIR $DATOMIC_HOME  
RUN echo DATOMIC HOME: $DATOMIC_HOME  
ENTRYPOINT ["./bin/transactor"]  
  
# 3. Provide a CMD argument with the relative path to the  
# transactor.properties file it will supplement the ENTRYPOINT  
VOLUME $DATOMIC_DATA  
  
EXPOSE 4334 4335 4336  

