# spidermonkey  
#  
# VERSION: see `TAG`  
FROM debian:jessie  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install deps  
RUN apt-get -y -qq update \  
&& apt-get -y -qq install zip unzip libnspr4-dev wget  
  
# download binary  
ENV SPIDER_ZIP jsshell-linux-x86_64.zip  
ENV SPIDER_ROOT /opt/src/jsshell  
RUN mkdir -p ${SPIDER_ROOT} \  
&& cd ${SPIDER_ROOT}/../ \  
&& wget http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-
trunk/${SPIDER_ZIP} \  
&& unzip ${SPIDER_ZIP} -d ${SPIDER_ROOT} \  
&& ln -s ${SPIDER_ROOT}/js /usr/local/bin \  
&& ln -s ${SPIDER_ROOT}/*.so /usr/local/share  
  
# cleanup temp  
RUN apt-get -y -qq --force-yes clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf ${SPIDER_ROOT}/../${SPIDER_ZIP}  
  
# configure execution  
ENTRYPOINT ["/usr/local/bin/js"]  
CMD ["-i"]  

