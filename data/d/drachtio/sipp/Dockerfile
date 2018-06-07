FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get -y --quiet --force-yes upgrade \  
&& apt-get install -y --no-install-recommends ca-certificates gcc g++ make
build-essential git wget libssl-dev libpcap-dev libncurses-dev \  
&& cd /usr/local/src \  
&& wget
https://sourceforge.net/projects/sipp/files/sipp/3.4/sipp-3.3.990.tar.gz \  
&& tar xvf sipp-3.3.990.tar.gz && cd sipp-3.3.990 && ./configure --with-pcap
&& make && make install \  
&& apt-get purge -y --quiet --force-yes --auto-remove ca-certificates gcc g++
make build-essential git wget \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
&& rm -Rf /var/log/* \  
&& rm -Rf /var/lib/apt/lists/* \  
&& cd /usr/local/src \  
&& rm -Rf * \  
&& mkdir /scenarios  
  
VOLUME ["/scenarios"]  
  
COPY ./entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["sipp"]  

