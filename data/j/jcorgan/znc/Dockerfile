FROM alpine  
label maintainer="johnathan@corganlabs.com"  
  
RUN apk update \  
&& apk add znc \  
&& apk add dumb-init \  
&& rm -rf /var/cache/apk/*  
  
RUN adduser -S user  
WORKDIR /home/user  
ENV HOME=/home/user  
USER user  
ENTRYPOINT ["/usr/bin/dumb-init", "/usr/bin/znc", "-f"]  

