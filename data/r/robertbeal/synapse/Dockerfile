FROM alpine:3.7  
MAINTAINER Robert Beal <rob@kohi.uk>  
  
ENV VERSION=v0.26.0  
ARG UID=3400  
ARG GID=3400  
  
RUN apk --no-cache add --virtual=build-dependencies \  
build-base \  
python2-dev \  
&& apk --no-cache add \  
ca-certificates \  
curl \  
py2-asn1 \  
py2-asn1-modules \  
py2-bcrypt \  
py2-cffi \  
py2-crypto \  
py2-cryptography \  
py2-dateutil \  
py2-decorator \  
py2-jinja2 \  
py2-jsonschema \  
py2-ldap3 \  
py2-msgpack \  
py2-netaddr \  
py2-openssl \  
py2-phonenumbers \  
py2-pillow \  
py2-pip \  
py2-psutil \  
py2-psycopg2 \  
py2-requests \  
py2-service_identity \  
py2-simplejson \  
py2-tz \  
py2-yaml \  
py-twisted \  
shadow \  
su-exec \  
&& pip install https://github.com/matrix-org/synapse/archive/$VERSION.tar.gz \  
&& apk del --purge build-dependencies \  
&& addgroup -g $GID synapse \  
&& adduser -u $UID -G synapse -S synapse \  
&& mkdir /config /data \  
&& chown -R synapse /config /data  
  
COPY entrypoint.sh /usr/local/bin  
VOLUME /config /data  
EXPOSE 8448 8008  
HEALTHCHECK --interval=30s --retries=3 CMD curl --fail http://localhost:8008
|| exit 1  
  
ENTRYPOINT ["entrypoint.sh"]  

