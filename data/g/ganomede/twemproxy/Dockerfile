FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
EXPOSE 6379 6222  
# Install Build then Uninstall in one step to minify the docker image  
RUN apt-get update \  
&& apt-get -qy install libtool make automake git \  
&& cd /tmp \  
&& git clone https://github.com/twitter/twemproxy.git \  
&& cd twemproxy \  
&& git checkout v0.4.0 \  
&& autoreconf -fvi \  
&& ./configure --prefix=/ \  
&& make -j2 \  
&& make install \  
&& cd .. \  
&& rm -fr twemproxy \  
&& apt-get remove -y libtool make automake git \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV REDIS_AUTH=""  
# Copy and install resources  
COPY twemproxy.yml.in run.sh /  
  
CMD [ "/run.sh" ]  

