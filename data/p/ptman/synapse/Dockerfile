# vim: set si ai et ft=dockerfile:  
FROM alpine:3.7  
# Author with no obligation to maintain  
MAINTAINER Paul Tötterman <paul.totterman@iki.fi>  
  
RUN apk --no-cache add \  
build-base \  
ca-certificates \  
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
py2-lxml \  
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
python2-dev \  
py-twisted \  
su-exec \  
&& pip install https://github.com/matrix-org/synapse/archive/v0.26.0.tar.gz \  
&& rm -rf /root/.cache \  
&& addgroup -g 333 -S synapse \  
&& adduser -u 333 -S -G synapse synapse  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /data  
EXPOSE 8448  
EXPOSE 8008  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["serve"]  

