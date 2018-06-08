  
FROM python:2.7-alpine  
  
MAINTAINER dianaesteves  
  
EXPOSE 5555  
ENV ALPYADB /alpyadb/  
WORKDIR ${ALPYADB}  
  
RUN /bin/echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN /bin/echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
RUN apk update  
RUN apk add eudev@edge \  
usbutils@edge \  
perl@edge \  
jq@edge \  
curl \  
file \  
imagemagick \  
libressl2.4-libcrypto@edge \  
android-tools@testing  
  
ENTRYPOINT [ "/usr/bin/adb" ]  
  
CMD [ "help" ]  

