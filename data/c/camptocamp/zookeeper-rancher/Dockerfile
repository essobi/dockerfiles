FROM zookeeper:3.4  
ENV CONFD_VERSION=0.12.0-alpha3 \  
RUNIT_VERSION=2.1.2  
RUN buildDeps='tar make gcc musl-dev' \  
RUNIT_DOWNLOAD_URL="http://smarden.org/runit/runit-${RUNIT_VERSION}.tar.gz" \  
RUNIT_DOWNLOAD_SHA1="398f7bf995acd58797c1d4a7bcd75cc1fc83aa66" \  
&& set -x \  
&& apk add --update curl $buildDeps \  
&& curl -sSL "$RUNIT_DOWNLOAD_URL" -o runit.tar.gz \  
&& echo "$RUNIT_DOWNLOAD_SHA1 *runit.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/runit \  
&& tar -xzf runit.tar.gz -C /usr/src/runit --strip-components=2 \  
&& rm -f runit.tar.gz \  
&& cd /usr/src/runit/src \  
&& make \  
&& cd .. \  
&& cat package/commands | xargs -I {} mv -f src/{} /sbin/ \  
&& cd / \  
&& rm -rf /usr/src/runit \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /service \  
;  
  
RUN curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
COPY ./confd.run /etc/service/confd/run  
COPY ./zookeeper.run /etc/service/zookeeper/run  
  
COPY ./conf.d /etc/confd/conf.d  
COPY ./templates /etc/confd/templates  
  
ENTRYPOINT [ "runsvdir", "-P", "/etc/service/" ]  

