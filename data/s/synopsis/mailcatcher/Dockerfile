FROM alpine:latest  
  
MAINTAINER developers@synopsis.cz  
  
RUN apk add --update build-base libstdc++ ruby ruby-dev ruby-bigdecimal sqlite
sqlite-dev \  
&& gem install json --no-ri --no-rdoc \  
&& gem install mailcatcher -v 0.5.12 --no-ri --no-rdoc \  
&& apk del --purge build-base ruby-dev \  
&& rm -rf /var/cache/apk/*  
  
# smtp port  
EXPOSE 1025  
# webserver port  
EXPOSE 1080  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

