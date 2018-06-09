FROM python:2-alpine  
  
LABEL maintainer="Simon Erhardt <hello@rootlogin.ch>" \  
org.label-schema.name="Matrix.org Synapse" \  
org.label-schema.description="Matrix.org reference implementation Synapse
packaged as docker image based on Alpine Linux." \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/chrootLogin/docker-matrix-
synapse" \  
org.label-schema.schema-version="1.0"  
  
ARG SYNAPSE_VERSION=0.27.4  
  
ENV REPORT_STATS=yes \  
SERVER_NAME=example.com  
  
RUN set -ex \  
&& apk add --update \  
alpine-sdk \  
bash \  
libffi \  
libffi-dev \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
linux-headers \  
postgresql \  
postgresql-dev \  
tini \  
# Install python stuff  
&& pip install --upgrade psycopg2 \  
&& pip install --upgrade pip \  
&& pip install --upgrade setuptools \  
&& pip install https://github.com/matrix-
org/synapse/tarball/v${SYNAPSE_VERSION} \  
# Remove build-time stuff  
&& apk del \  
alpine-sdk \  
libffi-dev \  
libjpeg-turbo-dev \  
linux-headers \  
postgresql-dev \  
&& rm -rf /var/cache/apk/*  
  
COPY root/ /  
  
VOLUME /data /config  
  
EXPOSE 8008 8448  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/docker-run.sh"]  

