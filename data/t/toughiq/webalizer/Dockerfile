FROM debian:stretch  
MAINTAINER toughiq <toughIQ@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y apt-utils webalizer \  
&& apt-get upgrade -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /usr/share/doc /usr/share/man /usr/share/locale /usr/share/info
/usr/share/lintian  
  
# we read logs from here  
VOLUME /logs  
  
# we write results to there  
VOLUME /webalizer  
  
COPY webalizer.conf /etc/webalizer.conf  
COPY run.sh /run.sh  
  
CMD ["/run.sh"]  
  
ENV DOMAIN=mydomain.com \  
LOGPREFIX=access \  
INTERVAL=3600 \  
VERBOSE=0  

