FROM rpawel/ubuntu:xenial  
  
RUN apt-get -q -y update \  
&& apt-get dist-upgrade -y --no-install-recommends \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
optipng jpegoptim parallel  
  
COPY optimize.sh /usr/local/bin/optimize.sh  
  

