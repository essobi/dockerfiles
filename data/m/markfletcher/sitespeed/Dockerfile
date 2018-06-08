FROM markfletcher/oracle-java7  
  
MAINTAINER Mark Fletcher  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y phantomjs curl xsltproc \  
&& DEBIAN_FRONTEND=noninteractive apt-get clean all \  
&& mkdir -p /usr/local/sitespeed/sitespeed-result \  
&& curl -SL
"https://github.com/sitespeedio/sitespeed.io/releases/download/v2.5.7/sitespeed.io-2.5.7.tar.gz"
-o sitespeed.io.tar.gz \  
&& tar -xzf sitespeed.io.tar.gz -C /usr/local/sitespeed --strip-components=1 \  
&& rm sitespeed.io.tar.gz  
WORKDIR /usr/local/sitespeed  
VOLUME /usr/local/sitespeed/sitespeed-result  
ENTRYPOINT ["/usr/local/sitespeed/bin/sitespeed.io"]  

