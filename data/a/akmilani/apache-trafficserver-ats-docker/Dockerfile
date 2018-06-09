FROM alpine:latest  
MAINTAINER Armin Khaghani Milani <armin.k.milani@gmail.com>  
  
RUN apk update \  
&& apk add --no-cache --update-cache curl ca-certificates file build-base git
libexecinfo-dev pcre-dev libressl-dev autoconf automake libtool tcl-dev
libunwind libunwind-dev linux-headers \  
&& apk --no-cache add hwloc hwloc-dev --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ \  
&& mkdir /opt \  
&& cd /tmp \  
&& git clone https://github.com/apache/trafficserver.git \  
&& cd /tmp/trafficserver* \  
&& autoreconf -if \  
&& ./configure --enable-experimental-plugins \  
&& make \  
&& make install \  
&& rm -rf /tmp/trafficserver* \  
&& apk del --purge build-base git autoconf automake  
  
RUN rm -rf /trafficserver/*.config  
ADD config/ /trafficserver/  
  
EXPOSE 80 443  
VOLUME ["/trafficserver"]  
LABEL type="ats" maintainer="armin.k.milani@gmail.com" department="ocdn"
name="ats"  
CMD ["/usr/local/bin/traffic_cop"]  

