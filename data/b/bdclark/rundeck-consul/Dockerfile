FROM alpine:3.6  
ENV RDECK_BASE=/opt/rundeck  
  
WORKDIR $RDECK_BASE  
  
# checksums at http://rundeck.org/downloads.html not necessarily accurate!  
ENV RDECK_VERSION 2.9.3  
ENV RDECK_CHECKSUM
eb848294ed0504fc6235e45d6bcfed32f352e7468c0a0f2068e87786f08e0188  
RUN \  
addgroup -S rundeck \  
&& adduser -S -H -G rundeck -D rundeck \  
&& apk --no-cache add \  
bash \  
curl \  
openjdk8-jre \  
openssh-client \  
python \  
su-exec \  
wget \  
&& python -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip install awscli \  
&& rm -r /root/.cache \  
&& curl -fLo rundeck-launcher.jar http://dl.bintray.com/rundeck/rundeck-
maven/rundeck-launcher-2.9.3.jar \  
&& echo "$RDECK_CHECKSUM rundeck-launcher.jar" | sha256sum -c  
  
# Run rundeck momemtarily in order to initialize directory structure  
RUN \  
java -jar rundeck-launcher.jar & \  
max=15 \  
&& failed=true \  
&& for i in $(seq 1 $max); do \  
if [ -f "$RDECK_BASE/etc/framework.properties" ]; then \  
failed=false; \  
break; \  
fi \  
&& sleep 10 \  
; done \  
&& if [ "$failed" = true ]; then echo "Rundeck failed to initialize"; exit 1;
fi \  
&& kill "$(jobs -p)" \  
&& rm server/logs/* \  
&& find $RDECK_BASE -not -name '*.jar' -print0 | xargs -0 chown rundeck:  
  
# Add dumb-init for proper PID 1 management  
ENV DUMB_INIT_VERSION 1.2.0  
RUN wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64" \  
&& wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/sha256sums" \  
&& grep "dumb-init_${DUMB_INIT_VERSION}_amd64$" sha256sums | sha256sum -c \  
&& rm sha256sums \  
&& mv dumb-init_${DUMB_INIT_VERSION}_amd64 /usr/bin/dumb-init \  
&& chmod +x /usr/bin/dumb-init  
  
# Add consul-template to manage configuration  
ENV CONSUL_TEMPLATE_VERSION 0.19.3  
RUN set -ex \  
&& apk add --no-cache --virtual .ctmpl-deps ca-certificates curl gnupg libcap
openssl \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
91A6E7F85D05C65630BEF18951852D87348FFC4C \  
&& mkdir -p /tmp/build \  
&& cd /tmp/build \  
&& wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig \  
&& gpg --batch --verify consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS.sig consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
&& grep consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS | sha256sum -c \  
&& unzip -d /bin consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& cd /tmp \  
&& rm -rf /tmp/build \  
&& apk del .ctmpl-deps \  
&& rm -rf /root/.gnupg  
  
ENV RDECK_HTTP_PORT=4440 \  
RDECK_HTTPS_PORT=4443 \  
CONSUL_PREFIX=service/rundeck  
  
COPY consul-template /etc/consul-template/  
COPY rdeck_base $RDECK_BASE/  
  
EXPOSE $RDECK_HTTP_PORT  
  
CMD ["/opt/rundeck/run.sh"]  

