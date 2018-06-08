#FROM java:7u91-jre-alpine  
FROM williamyeh/java7  
  
MAINTAINER Gaetan Warmont (gwa@n-side.com)  
  
ENV SBT_VERSION 0.13.8  
ENV SBT_JAR https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar  
# ENV PATH ${PATH}:/usr/local/bin  
  
ADD $SBT_JAR /usr/local/bin/sbt-launch.jar  
COPY sbt.sh /usr/local/bin/sbt  
  
#RUN apk update && apk --no-cache add \  
# curl openssl ca-certificates  
  
# RUN echo "==> fetch all sbt jars from Maven repo..." && \  
# echo "==> [CAUTION] this may take several minutes!!!" && \  
# sbt  
  
# Add phantomjs  
# Sbt ivy cahce has to be persisted  
VOLUME [ "/app" , "/sbt/.ivy2"]  
# If you want to persist ivy cache create a Container volume like that:  
# docker run -v /sbt/.ivy2 --name sbtcache williamyeh/java7 echo "Sbt cache
volume created"  
  
# phantomjs installation  
# ENV PHANTOMJS_VERSION 2.1.1  
# RUN \  
# apt-get update && \  
# apt-get upgrade -y && \  
# apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \  
# mkdir -p /srv/var && \  
# wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
# tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
# rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
# mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
# ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
# git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
# ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
# apt-get autoremove -y && \  
# apt-get clean all  
  
WORKDIR /app  
  
# Define default command.  
ENTRYPOINT ["sbt"]  
#CMD ["--version"]  

