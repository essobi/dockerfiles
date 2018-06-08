FROM openjdk:8-jre-alpine  
  
ENV SBT_VERSION 0.13.8  
RUN apk add --no-cache bash curl redis  
  
# setup redis  
RUN mkdir /data && chown redis:redis /data && \  
sed 's/^bind 127.0.0.1/bind 0.0.0.0/' -i /etc/redis.conf && \  
sed 's/^daemonize no/daemonize yes/' -i /etc/redis.conf && \  
sed 's/^protected-mode yes/protected-mode no/' -i /etc/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis.conf  
VOLUME /data  
  
# setup sbt  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt  
  
RUN redis-server /etc/redis.conf && sbt  

