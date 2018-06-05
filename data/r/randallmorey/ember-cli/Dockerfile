FROM mhart/alpine-node:8.4.0  
MAINTAINER Randall Morey <randall@randallmorey.com>  
  
ENV EMBER_CLI_VERSION=2.14.2 \  
REQUIRED_PACKAGES="curl git python build-base" \  
PHANTOMJS_ARCHIVE="phantomjs.tar.gz"  
  
RUN apk --update add ${REQUIRED_PACKAGES} && \  
# install phantomjs  
curl -Lk -o $PHANTOMJS_ARCHIVE https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \  
&& tar -xf $PHANTOMJS_ARCHIVE -C /tmp/ \  
&& cp -R /tmp/etc/fonts /etc/ \  
&& cp -R /tmp/lib/* /lib/ \  
&& cp -R /tmp/lib64 / \  
&& cp -R /tmp/usr/lib/* /usr/lib/ \  
&& cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ \  
&& cp -R /tmp/usr/share/* /usr/share/ \  
&& cp /tmp/usr/local/bin/phantomjs /usr/bin/ \  
&& rm -fr $PHANTOMJS_ARCHIVE /tmp/* && \  
# install ember cli  
npm install -g ember-cli@${EMBER_CLI_VERSION} && \  
rm -rf /tmp/* /var/cache/apk/* /root/.npm  
  
EXPOSE 3000 4200 49152  
WORKDIR /ember-cli-app  
  
ENTRYPOINT ["/usr/bin/ember"]  

