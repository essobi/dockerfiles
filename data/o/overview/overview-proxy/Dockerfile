FROM haproxy:1.7.9-alpine  
  
ENV ACMETOOL_VERSION=0.0.61 \  
ACMETOOL_SHA1=c166832b15f8ed653ae300754eac2d4bdb009d08  
  
RUN set -x \  
&& apk \--no-cache add openssl ca-certificates \  
&& wget -q -O acmetool.tar.gz
"https://github.com/hlandau/acme/releases/download/v0.0.61/acmetool-v$ACMETOOL_VERSION-
linux_amd64.tar.gz" \  
&& echo "$ACMETOOL_SHA1 *acmetool.tar.gz" | sha1sum -c \  
&& mkdir -p /usr/src/acmetool \  
&& tar -zxf acmetool.tar.gz -C /usr/src/acmetool --strip-components=1 \  
&& install -m0755 /usr/src/acmetool/bin/acmetool /usr/bin/ \  
&& mkdir -p /usr/share/man/man8 \  
&& install -D /usr/src/acmetool/doc/acmetool.8 /usr/share/man/man8/acmetool.8
\  
&& rm -r acmetool.tar.gz /usr/src/acmetool  
  
EXPOSE 80 443 9000 3000 3001 3003 3004 3005  
COPY haproxy.cfg maintain-ssl-certs acme-responses.yml overview-proxy _dummy-
cert-just-to-make-haproxy-load.pem /  
CMD [ "/overview-proxy" ]  

