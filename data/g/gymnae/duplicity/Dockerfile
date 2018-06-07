FROM gymnae/alpine-base:master  
MAINTAINER Gunnar Falk <docker@grundstil.de>  
  
# install base packages  
RUN apk-install \  
duply \  
py-boto \  
openssl \  
py-crypto \  
py-pip \  
grep \  
&& adduser -D -u 1999 duplicity \  
&& chmod -R go+rwx /home/duplicity/  
  
# workaround for alpine linux missing py-fasterners  
RUN pip install fasteners  
  
ENV HOME=/home/duplicity  
#VOLUME /home/duplicity/.cache/duplicity  
#VOLUME /home/duplicity/.gnupg  
# prepare init script for start  
ADD init.sh /init.sh  
ADD conf /tmp/conf  
RUN chmod +x /init.sh  
CMD ["/init.sh"]  

