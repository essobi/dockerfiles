# minimal figlet  
#  
FROM alpine  
MAINTAINER Mike  
  
RUN apk update \  
&& apk upgrade \  
&& apk add figlet \  
#  
# clean up cached artefacts  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["figlet"]  

