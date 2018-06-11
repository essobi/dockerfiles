FROM alpine:latest  
MAINTAINER whywaita <whywaita@whywrite.it>  
  
RUN apk add --no-cache coreutils curl \  
&& curl "https://raw.githubusercontent.com/uecmma/meshi/master/meshi" -o
/bin/meshi \  
&& chmod +x /bin/meshi  
  
CMD /bin/meshi  

