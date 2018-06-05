  
FROM alpine:3.7  
  
ENV \  
TERM=xterm \  
BUILD_DATE="2018-01-24" \  
FLUENTD_VERSION="1.0" \  
FLUENTD_OPT=""  
  
EXPOSE 24224 5140  
  
LABEL \  
version="1801" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="fluentd Docker Image" \  
org.label-schema.description="Inofficial fluentd Docker Image" \  
org.label-schema.url="https://fluentd.io/" \  
org.label-schema.vcs-url="https://github.com/bodsch/fluentd" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
  
WORKDIR /fluent  
  
#
---------------------------------------------------------------------------------------  
  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache --virtual .build-deps \  
gcc \  
g++ \  
make \  
ruby-dev \  
shadow && \  
apk add \  
ca-certificates \  
ruby \  
ruby-irb && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
gem install \  
fluentd -v ${FLUENTD_VERSION} && \  
gem install \  
oj \  
json \  
gelf \  
fluent-plugin-secure-forward \  
fluent-plugin-copy_ex \  
fluent-plugin-elasticsearch \  
fluent-plugin-concat \  
fluent-plugin-graylog && \  
adduser -D -g '' -u 1000 -h /home/fluent fluent && \  
mkdir -p \  
/fluentd/etc\  
/fluentd/log \  
/fluentd/plugins && \  
chown -R fluent: /fluentd && \  
apk del .build-deps && \  
rm -rf \  
/var/cache/apk/* \  
/tmp/* \  
/var/tmp/* \  
/root/.gem \  
/usr/lib/ruby/gems/*/cache/*.gem  
  
COPY rootfs /  
  
# CMD [ "/bin/sh" ]  
  
CMD fluentd --config /etc/fluentd.conf --plugin /fluentd/plugins
${FLUENTD_OPT}  
  
# EOF  

