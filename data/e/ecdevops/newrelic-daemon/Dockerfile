FROM debian:sid  
MAINTAINER Web Team <webdev@ecenglish.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add \- \  
&& echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list \  
&& apt-get update \  
&& apt-get install -y newrelic-php5 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD start.sh /tmp/start.sh  
  
ENTRYPOINT /tmp/start.sh  

