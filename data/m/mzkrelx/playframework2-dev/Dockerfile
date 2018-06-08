# mzkrelx/playframework2-dev  
#  
# VERSION 0.0.1  
FROM centos  
MAINTAINER Mizuki Yamanaka <mizuki@relx.jp>  
  
ENV PLAY_VERSION 2.2.3  
ENV PATH $PATH:/opt/play-$PLAY_VERSION  
  
RUN yum install -y unzip java-1.7.0-openjdk-devel && yum clean all  
ADD http://downloads.typesafe.com/play/$PLAY_VERSION/play-$PLAY_VERSION.zip
/tmp/play-$PLAY_VERSION.zip  
RUN (cd /opt && unzip /tmp/play-$PLAY_VERSION.zip && rm -f
/tmp/play-$PLAY_VERSION.zip)  
  
VOLUME ["/opt/workspace"]  
WORKDIR /opt/workspace  
EXPOSE 9000  
CMD ["/bin/bash"]  
  

