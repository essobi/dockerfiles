FROM tomcat:9-alpine  
MAINTAINER fujii.kazunobu@gmail.com  
  
ENV OPENGROK_DIRECTORY /usr/opengrok  
ENV OPENGROK_INSTANCE_BASE /var/opengrok  
  
RUN apk add \--no-cache \--virtual .ctag-build-deps gcc g++ make \  
&& cd / \  
&& wget -O -
http://hp.vector.co.jp/authors/VA025040/ctags/downloads/ctags-5.8j2.tar.gz |
tar zxvf - \  
&& mv ctags-* ctags \  
&& cd /ctags/ \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /ctags \  
&& apk del .ctag-build-deps \  
&& apk add \--no-cache \--virtual .opengrok-install-deps ca-certificates
openssl \  
&& cd / \  
&& wget -O -
https://github.com/OpenGrok/OpenGrok/releases/download/1.0/opengrok-1.0.tar.gz
| tar zxvf - \  
&& mv opengrok-* $OPENGROK_DIRECTORY \  
&& apk del .opengrok-install-deps \  
&& mkdir -p $OPENGROK_INSTANCE_BASE \  
&& OPENGROK_TOMCAT_BASE=$CATALINA_HOME $OPENGROK_DIRECTORY/bin/OpenGrok deploy  

