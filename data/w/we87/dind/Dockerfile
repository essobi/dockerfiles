FROM jpetazzo/dind  
MAINTAINER antmanler@gmail.com  
  
# s6  
ENV S6_VERSION v1.11.0.1  
RUN curl -L https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
| tar -C / -xzf -  
  
# for artifacts  
VOLUME /we87  
  
ENV SS_VER 2.4.2  
ENV SS_URL https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz  
ENV SS_DIR shadowsocks-libev-$SS_VER  
ENV SS_DEP git-core build-essential autoconf libtool libssl-dev  
  
RUN apt-get update \  
&& apt-get install -y $SS_DEP curl iptables ipset \  
&& cd /tmp \  
&& curl -sSL $SS_URL | tar xz \  
&& cd $SS_DIR \  
&& ./configure \  
&& make install \  
&& cd .. \  
&& rm -rf $SS_DIR \  
&& apt-get --purge autoremove -y $SS_DEP \  
&& apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*  
  
# add services  
COPY s6 /etc/  
COPY ss /etc/ss/  
COPY run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  
ENV PORT 2375  
CMD /usr/local/bin/wrapdocker  

