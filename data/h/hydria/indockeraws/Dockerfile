FROM docker:latest  
  
ENV PACKAGES="\  
awscli \  
bash"  
RUN echo \  
# replacing default repositories with edge ones  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
  
# Add the packages, with a CDN-breakage fallback if needed  
&& apk add \--no-cache $PACKAGES || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache
$PACKAGES) \  

