# Dockerfile for Deluge, with Alpine Base  
FROM alpine:3.2  
MAINTAINER mlindsey@fastmail.com.au  
  
# Add additional repo's to APK  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
# RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
# RUN echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
# Install Dependancies and Application  
RUN apk update  
RUN apk add bash py-pip deluge@testing && \  
rm -rf /var/cache/apk/*  
  
# Add additional files.  
ADD assets/config /config  
ADD assets/startdeluge /usr/local/bin/startdeluge  
ADD assets/requirements.txt /requirements.txt  
RUN pip install --upgrade && pip install --upgrade setuptools && pip install
enum34 service_identity -r /requirements.txt  
RUN chmod 777 /usr/local/bin/startdeluge  
RUN chmod 777 /config  
RUN mkdir /torrents && chmod 777 /torrents  
  
# Expose Ports  
EXPOSE 53160  
EXPOSE 53160/udp  
EXPOSE 8112  
EXPOSE 58846  
# Default command to run  
CMD ["/usr/local/bin/startdeluge"]  

