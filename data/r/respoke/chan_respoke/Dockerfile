# -*- Dockerfile -*-  
FROM respoke/asterisk  
MAINTAINER Respoke <info@respoke.io>  
  
ENV CHAN_RESPOKE_VERSION=v1.1.0  
RUN mkdir -p /usr/src/chan_respoke && \  
cd /usr/src/chan_respoke && \  
curl -vsL
https://github.com/respoke/chan_respoke/archive/${CHAN_RESPOKE_VERSION}.tar.gz
| \  
tar --strip-components 1 -xz && \  
make all install && \  
install -m 644 example/sounds/respoke* /var/lib/asterisk/sounds/ && \  
sed 's#^;dtls_cert_file=.*$#dtls_cert_file=/etc/asterisk/keys/respoke.pem#'
respoke.conf.sample > /etc/asterisk/respoke.conf && \  
rm -rf /usr/src/chan_respoke  
  
RUN echo "#include modules-respoke.conf" >> /etc/asterisk/modules.conf  
COPY conf/ /etc/asterisk/  
COPY chan_respoke-docker-entrypoint.sh /  
ENTRYPOINT ["/chan_respoke-docker-entrypoint.sh"]  
CMD ["/usr/sbin/asterisk", "-f"]  

