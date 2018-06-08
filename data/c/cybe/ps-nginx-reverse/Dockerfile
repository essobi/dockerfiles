FROM cybe/ps-nginx-base:alpine37  
  
# Generate trusted certificates for OSCP stapling  
RUN apk --no-cache add --virtual .fetch-deps openssl html-xml-utils \  
&& CERT=/etc/nginx/le-ca-certs.crt \  
&& wget -O - https://letsencrypt.org/certs/isrgrootx1.pem | sed 's/\r//g' >>
${CERT} \  
&& wget -O - https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem >>
${CERT} \  
&& wget -O - https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.pem >>
${CERT} \  
&& echo "-----BEGIN CERTIFICATE-----" >> ${CERT} \  
&& wget -O - https://www.identrust.com/certificates/trustid/root-
download-x3.html \  
| hxnormalize -x | hxselect -c "textarea[name=cert]" | sed -e 's/[\r ]//g' -e
'1d' >> ${CERT} \  
&& echo "-----END CERTIFICATE-----" >> ${CERT} \  
&& apk del --purge .fetch-deps  
  
COPY configs/ssl_params configs/proxy_params /etc/nginx/  
COPY configs/strict_https configs/strict_sni /etc/nginx/conf.d/  
COPY sites/dl.pinshot.net sites/files.pinshot.net sites/hub.pinshot.net
sites/www.pinshot.net sites/home.pinshot.net /etc/nginx/sites/  

