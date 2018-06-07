FROM golang:alpine  
  
RUN apk add --no-cache --update python \  
&& rm -rf /usr/include /usr/lib/python2.7/idlelib \  
&& find /usr/lib/python2.7 -type d -name "tests" | xargs rm -rf \  
&& find /usr/lib/python2.7 -name "*.py[co]" -delete -o -name "*.exe" -delete  

