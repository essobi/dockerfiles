FROM alpine:latest  
MAINTAINER Philipp Hellmich <phil@hellmi.de>  
  
# both groff and less are for `help` subcommands  
RUN apk add --update python py-pip groff less wget tar ca-certificates openssl
gnupg\  
&& pip install awscli \  
&& rm -rf /usr/lib/python2.7/distutils \  
/usr/lib/python2.7/idlelib \  
/usr/lib/python2.7/lib-tk \  
/usr/lib/python2.7/ensurepip \  
/usr/lib/python2.7/pydoc_data \  
/var/cache/apk/*  
  
# install dumb init  
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.1.0/dumb-
init_1.1.0_amd64 \  
-O /usr/local/bin/dumb-init \  
&& chmod +x /usr/local/bin/dumb-init  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
VOLUME ["/.aws", "/backup"]  
# Server CMD  
CMD ["dumb-init", "/run.sh"]  

