FROM ubuntu:14.04  
MAINTAINER MidoNet (https://www.midonet.org)  
  
ADD conf/midonet.list /etc/apt/sources.list.d/midonet.list  
  
RUN set -xe \  
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv \  
E9996503AEB005066261D3F38DDA494E99143E75 \  
&& apt-get -qy update \  
&& apt-get -qy dist-upgrade \  
\  
&& apt-get -qy install software-properties-common \  
&& add-apt-repository -y ppa:openjdk-r/ppa \  
&& apt-get -qy update \  
&& apt-get -qy install openjdk-8-jre --no-install-recommends \  
\  
&& apt-get -qy install midonet-tools \  
python-midonetclient \  
\  
&& apt-get -qy remove \--auto-remove software-properties-common \  
&& rm -fr /var/lib/apt/lists/* /etc/apt/sources.list.d/* \  
\  
&& mkdir -p /home/midonet \  
&& mkdir -p /etc/midonet \  
&& touch /etc/midonet_host_id.properties \  
&& groupadd -r midonet -g 413 \  
&& useradd -u 411 -r -g midonet -d /home/midonet -s /sbin/nologin -c \  
"MidoNet utils docker image user" midonet \  
&& chown -R midonet:midonet /home/midonet /etc/midonet \  
/etc/midonet_host_id.properties  
  
ADD scripts/run-cmd.sh /cli  
  
ENV ZK_ENDPOINTS="127.0.0.1:2181"  
ENV CLUSTER_URL="http://127.0.0.1:8181"  
ENV USERNAME="admin"  
ENV PASSWORD="admin"  
ENV PROJECT="admin"  
ENV UUID=""  
  
USER midonet  
  
ENTRYPOINT ["/cli"]  

