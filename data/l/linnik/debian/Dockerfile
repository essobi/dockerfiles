FROM debian:jessie  
MAINTAINER Vyacheslav Linnik <vyacheslav.linnik@gmail.com>  
  
ENV UTIL_LINUX_URL https://www.kernel.org/pub/linux/utils/util-linux  
ENV UTIL_LINUX_VERSION v2.27/util-linux-2.27.tar.gz  
  
RUN set -x \  
&& apt-get update -y \  
&& deps='make gcc curl' \  
&& apt-get install -y $deps \  
&& curl $UTIL_LINUX_URL/$UTIL_LINUX_VERSION -o /tmp/util-linux.tar.gz \  
&& cd /tmp && tar -xf /tmp/util-linux.tar.gz \  
&& rm /tmp/util-linux.tar.gz \  
&& cd /tmp/util-linux-*/ \  
&& ./configure && make logger \  
&& cp /usr/bin/logger /usr/bin/logger.old \  
&& cp ./logger /usr/bin/logger \  
&& rm -rf /tmp/util-linux-* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $deps  

