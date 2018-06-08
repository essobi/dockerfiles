FROM greatbsky/openjdkx:latest  
MAINTAINER architect.bian  
LABEL name="flume" license="MIT" build-date="20180124"  
  
ENV VERSION 1.8.0  
ENV FLUME_HOME /data/env/flume  
ENV FLUME_URL http://archive.apache.org/dist/flume/$VERSION/apache-
flume-$VERSION-bin.tar.gz  
ENV PATH $PATH:$FLUME_HOME/bin:  
  
RUN yum update -y && cd /data/softs && wget "$FLUME_URL" && tar -zvxf apache-
flume-$VERSION-bin.tar.gz && mv /data/softs/apache-flume-$VERSION-bin
/data/env/flume && rm -rf /data/softs/* && (touch /var/log/log0 & touch
/var/log/log1 & touch /var/log/log2 & touch /var/log/log3 & touch
/var/log/log4 & touch /var/log/log5 & touch /var/log/log6 & touch
/var/log/log7 & touch /var/log/log8 & touch /var/log/log9)  
  
ADD flume.conf /data/env/flume/conf/flume.conf  
ADD startup.sh /usr/bin/startup.sh  
  
ENTRYPOINT [ "/usr/bin/startup" ]  

