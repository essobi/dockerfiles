FROM alpine:latest  
MAINTAINER anklebiter87@gmail.com  
  
#update  
RUN apk update && apk upgrade  
  
#install wget  
RUN apk add wget  
  
#adding unpackers  
RUN apk add unzip unrar p7zip  
  
#add nzbget user  
RUN addgroup -g 1000 nzbget && adduser -H -D -G nzbget -s /bin/false -u 1000
nzbget  
  
# create the install dir and volume mount points  
RUN mkdir /nzbget && mkdir /config && mkdir /downloads && mkdir /completed &&
mkdir /setup  
  
#will use this to check if a config is there or not  
COPY config-check.sh /setup/  
  
# download the latest nzbget version  
RUN wget -O - http://nzbget.net/info/nzbget-version-linux.json | sed -n
"s/^.*stable-download.*: \"\\(.*\\)\".*/\1/p" | wget --no-check-certificate -i
- -O /setup/nzbget-latest-bin-linux.run  
  
# install nzbget  
RUN /bin/sh /setup/nzbget-latest-bin-linux.run --destdir /nzbget  
  
# checking / makes a new config  
RUN chmod +x /setup/config-check.sh  
RUN /setup/config-check.sh  
  
# change the owner  
RUN chown -R nzbget:nzbget /nzbget /config /downloads /completed  
  
#clean up  
RUN rm -rf /setup  
RUN apk del wget  
RUN rm -rf /var/cache/apk/*  
  
# volumes  
VOLUME /config /downloads  
  
# exposes nzbget's default port  
EXPOSE 6789  
# not root anymore going forward  
USER nzbget  
  
# set some defaults and start nzbget in server and log mode  
ENTRYPOINT ["/nzbget/nzbget", "-s", "-o", "OutputMode=log", "-c",
"/config/nzbget.conf"]  

