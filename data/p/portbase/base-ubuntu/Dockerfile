FROM ubuntu:17.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y openssl curl tzdata \  
&& apt-get clean \  
&& ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
ENV DOCKERFY_SHA256
033477a642fa5ef3004c398cd13757edb92332852210e365ff6c02e91fe46eec  
RUN curl -sL
https://github.com/r-kok/dockerfy/releases/download/1.0.7-awssecret/dockerfy
-o /bin/dockerfy \  
&& echo "${DOCKERFY_SHA256} */bin/dockerfy" | sha256sum -c - \  
&& chmod +x /bin/dockerfy  

