FROM clojure:lein-2.6.1-alpine  
  
MAINTAINER Christian Romney "cromney@pointslope.com"  
ENV DATOMIC_VERSION 0.9.5561  
ENV DATOMIC_HOME /opt/datomic-pro-$DATOMIC_VERSION  
  
RUN apk add --no-cache unzip curl  
  
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
  
WORKDIR $DATOMIC_HOME  
  
# 3. Provide a CMD with an alias to the database  
# and the database uri  
# e.g. CMD ["dev", "datomic:dev://db:4334/"]  
ENTRYPOINT ["bin/console", "-p", "9000"]  
  
EXPOSE 9000  

