FROM quay.io/pires/docker-jre:8u92  
MAINTAINER pjpires@gmail.com  
  
ENV LOGSTASH_PKG_NAME logstash-2.3.2  
# Install Logstash  
RUN apk add --update curl bash ca-certificates  
RUN \  
( curl -Lskj
http://download.elastic.co/logstash/logstash/$LOGSTASH_PKG_NAME.tar.gz | \  
gunzip -c - | tar xf - ) && \  
mv $LOGSTASH_PKG_NAME /logstash && \  
rm -rf $(find /logstash | egrep
"(\\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))")
&& \  
apk del curl wget  
  
# Logstash config  
VOLUME ["/logstash/config"]  
COPY config/logstash.conf /logstash/config/  
COPY run.sh /  
RUN chmod +x /run.sh  
# Optional certificates folder  
VOLUME ["/logstash/certs"]  
CMD ["/run.sh"]  

