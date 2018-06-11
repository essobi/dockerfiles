# SSL cert generator  
FROM pgarrett/openssl-alpine AS cert-generator  
WORKDIR /certs  
RUN echo -e "[dn]\nCN=localhost\n[req]\ndistinguished_name =
dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth"
> openssl.cnf \  
&& openssl req \  
-x509 \  
-out localhost.crt \  
-keyout localhost.key \  
-newkey rsa:2048 \  
-nodes \  
-sha256 \  
-days 365 \  
-subj '/CN=localhost' \  
-extensions EXT \  
-config openssl.cnf  
  
# Nginx + static html  
FROM nginx:1.13.12-alpine  
  
RUN mkdir -p /etc/nginx/ssl  
  
COPY \--from=cert-generator /certs/localhost.key /etc/nginx/ssl  
COPY \--from=cert-generator /certs/localhost.crt /etc/nginx/ssl  
COPY default.conf /etc/nginx/conf.d  
COPY html /usr/share/nginx/html

