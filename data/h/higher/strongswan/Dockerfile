FROM buildpack-deps:jessie  
  
RUN mkdir -p /conf  
  
RUN apt-get update && apt-get install -y \  
libgmp-dev \  
iptables \  
xl2tpd \  
module-init-tools \  
supervisor  
  
ENV STRONGSWAN_VERSION 5.5.0  
ENV GPG_KEY 948F158A4E76A27BF3D07532DF42C170B34DBA77  
  
RUN mkdir -p /usr/src/strongswan \  
&& cd /usr/src \  
&& curl -SOL
"https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz.sig" \  
&& curl -SOL
"https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify strongswan-$STRONGSWAN_VERSION.tar.gz.sig
strongswan-$STRONGSWAN_VERSION.tar.gz \  
&& tar -zxf strongswan-$STRONGSWAN_VERSION.tar.gz -C /usr/src/strongswan
--strip-components 1 \  
&& cd /usr/src/strongswan \  
&& ./configure --prefix=/usr --sysconfdir=/etc \  
\--enable-eap-radius \  
\--enable-eap-mschapv2 \  
\--enable-eap-identity \  
\--enable-eap-md5 \  
\--enable-eap-mschapv2 \  
\--enable-eap-tls \  
\--enable-eap-ttls \  
\--enable-eap-peap \  
\--enable-eap-tnc \  
\--enable-eap-dynamic \  
\--enable-xauth-eap \  
\--enable-openssl \  
&& make -j \  
&& make install \  
&& rm -rf "/usr/src/strongswan*"  
  
# Strongswan Configuration  
COPY ipsec.conf /etc/ipsec.conf  
COPY strongswan.conf /etc/strongswan.conf  
  
# XL2TPD Configuration  
COPY xl2tpd.conf /etc/xl2tpd/xl2tpd.conf  
COPY options.xl2tpd /etc/ppp/options.xl2tpd  
  
# Supervisor config  
COPY supervisord.conf supervisord.conf  
COPY kill_supervisor.py /usr/bin/kill_supervisor.py  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY scripts /usr/local/bin  
  
# The password is later on replaced with a random string  
ENV USER user  
ENV PASSWORD password  
ENV PSK password  
  
VOLUME ["/etc/ipsec.d"]  
  
EXPOSE 4500/udp 500/udp 1701/udp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/supervisord.conf"]  

