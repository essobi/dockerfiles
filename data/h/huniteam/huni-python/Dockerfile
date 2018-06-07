FROM debian:wheezy  
  
WORKDIR /build  
COPY /build/ /build/  
  
ARG APT_MIRROR=&  
  
RUN sed -i -e "s!http://httpredir.debian.org/debian!$APT_MIRROR!" \  
/etc/apt/sources.list \  
&& apt-get update \  
&& /build/pypkg.sh build \  
&& /build/pypkg.sh install \  
&& apt-get clean \  
&& rm -rf /build \  
&& echo ok.  
  
ENV TZ=Australia/Melbourne  

