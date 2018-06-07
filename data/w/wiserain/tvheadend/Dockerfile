# package version  
ARG BASE_IMAGE  
FROM $BASE_IMAGE  
MAINTAINER wiserain  
  
# default variables  
ENV EPG2XML_VER="latest"  
ENV EPG_PORT="9983"  
ENV TZ="Asia/Seoul"  
# copy local files  
COPY root/ /  
  
# set permissions on tv_grab_files  
RUN chmod 555 /usr/bin/tv_grab_kr_*  
  
# remove irrelevant grabber  
RUN xargs rm < /tmp/tv_grab_irr.list  
  
# install dependencies for epg2xml  
RUN apk add --no-cache php7 php7-json php7-dom php7-mbstring php7-openssl
php7-curl jq  
  
# install dependencies for tvhProxy  
RUN apk add --no-cache py-flask py-requests py-gevent  
  
# cleanup  
RUN rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
# ports and volumes  
EXPOSE 9981 9982  
VOLUME /config /recordings /epg2xml  
WORKDIR /epg2xml  

