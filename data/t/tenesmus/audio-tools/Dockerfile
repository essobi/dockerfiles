FROM debian:stretch  
LABEL maintainer Nathan Douglas <github@tenesm.us>  
RUN set -xe \  
&& mkdir -p /data \  
&& echo "deb http://www.deb-multimedia.org stretch main non-free" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated \  
bash \  
cuetools \  
curl \  
flac \  
lame \  
libmac2 \  
monkeys-audio \  
shntool \  
&& echo Built successfully!  
WORKDIR /data  
  
  

