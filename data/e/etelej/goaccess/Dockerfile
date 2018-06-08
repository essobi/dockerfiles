FROM debian:jessie  
MAINTAINER Peter Etelej <peter@etelej.com>  
  
ENV PATH="/goaccess-1.2:${PATH}"  
  
RUN apt-get update && apt-get upgrade --no-install-recommends -y \  
&& apt-get install -y wget build-essential libncursesw5-dev libgeoip-dev \  
&& wget https://github.com/peteretelej/goaccess-
docker/releases/download/GoAccessv1.2/goaccess-1.2.tar.gz \  
&& tar -xzf goaccess-1.2.tar.gz \  
&& cd goaccess-1.2/ \  
&& ./configure --enable-utf8 --enable-geoip=legacy \  
&& make \  
&& make install \  
&& apt-get purge --auto-remove -y wget build-essential libncursesw5-dev
libgeoip-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
  
CMD ["goaccess"]  
  
  

