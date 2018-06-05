FROM ubuntu:xenial  
MAINTAINER MidoNet (https://www.midonet.org)  
  
ADD conf/midonet.list /etc/apt/sources.list.d/midonet.list  
  
RUN set -xe \  
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv \  
E9996503AEB005066261D3F38DDA494E99143E75 \  
&& apt-get -qy update \  
\  
&& apt-get -qy install midolman --no-install-recommends \  
\  
&& apt-get -qy install python-midonetclient curl  
  
ADD scripts/run-midolman.sh /agent  
  
# Expose bgpd port in case it is a gateway  
EXPOSE 179  
ENV ZK_ENDPOINTS="127.0.0.1:2181"  
ENV TEMPLATE="compute.large"  
ENV UUID=""  
ENV INIT_WAIT_TIME="60"  
ENV MIDONET_API_URL="http://localhost:8181/midonet-api"  
VOLUME /var/log/midolman  
  
CMD ["/agent"]  

