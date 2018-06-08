FROM alpine:3.6  
MAINTAINER Jia Huang <iamfat@gmail.com>  
  
RUN echo "http://dl-5.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --update add sphinx && rm -rf /var/cache/apk/* \  
&& mkdir -p /var/lib/sphinx/data \  
&& mkdir -p /var/log/sphinx \  
&& mkdir -p /var/run/sphinx  
  
ADD sphinx.conf.sh /etc/sphinx/sphinx.conf.sh  
  
# VOLUME ["/var/lib/sphinx", "/var/log/sphinx", "/var/run/sphinx"]  
# 9312 Sphinx Plain Port  
# 9306 SphinxQL Port  
EXPOSE 9312 9306  
CMD ["/usr/bin/searchd", "--nodetach", "--config",
"/etc/sphinx/sphinx.conf.sh"]  

