FROM node:7.10.0-alpine  
  
ARG VERSION=3.7.2  
RUN apk --no-cache add bash ca-certificates curl g++ git make openssl python
tini  
  
RUN mkdir -p /opt /var/lib/data/auth0-adldap  
  
RUN curl -Lo /tmp/adldap.tar.gz https://github.com/auth0/ad-ldap-
connector/archive/v$VERSION.tar.gz && \  
tar -xzf /tmp/adldap.tar.gz -C /tmp && \  
mv /tmp/ad-ldap-connector-$VERSION /opt/auth0-adldap  
  
RUN cd /opt/auth0-adldap && \  
npm install && \  
chown -R node /opt/auth0-adldap /var/lib/data/auth0-adldap && \  
npm cache clean && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# Copy app  
COPY ./scripts/entrypoint.sh /opt/auth0-adldap  
COPY ./scripts/healthcheck.py /opt/auth0-adldap  
  
ENTRYPOINT ["/sbin/tini", "--", "/opt/auth0-adldap/entrypoint.sh"]  
  
USER node  
WORKDIR /opt/auth0-adldap  
  
CMD node server.js

