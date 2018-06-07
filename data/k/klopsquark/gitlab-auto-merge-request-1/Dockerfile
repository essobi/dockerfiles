FROM alpine:3.6  
MAINTAINER Robert G <klopsquark@googlemail.com>  
  
RUN apk add --no-cache \  
bash \  
curl \  
grep \  
jq  
  
COPY merge-request.sh /usr/bin/  
  
CMD ["merge-request.sh"]  

