FROM alpine:3.4  
MAINTAINER Greg Feigenson <greg.feigenson@8x8.com>  
  
ENV KIBANA_VERSION=4.6.3 KIBANA_HOME=/usr/share/kibana
PATH=${PATH}:${KIBANA_HOME}/bin  
  
RUN apk update && apk upgrade && apk add --no-cache curl nodejs bash && \  
curl -Ls https://download.elastic.co/kibana/kibana/kibana-$KIBANA_VERSION-
linux-x86_64.tar.gz | tar -xz -C /usr/share && \  
ln -s /usr/share/kibana-$KIBANA_VERSION-linux-x86_64 $KIBANA_HOME && \  
  
# We can't use the standard NPM/Node distributed with Kibana because we're not
using glibc.  
# So let's grab one out of APK and symlink the distro. This is actually
smaller than  
# using APK to grab libuv et al and then remove Node.js after...  
rm $KIBANA_HOME/node/bin/npm && \  
rm $KIBANA_HOME/node/bin/node && \  
ln -s /usr/bin/npm $KIBANA_HOME/node/bin/npm && \  
ln -s /usr/bin/node $KIBANA_HOME/node/bin/node && \  
  
# Install all our plugins.  
$KIBANA_HOME/bin/kibana plugin --install elasticsearch/marvel/latest && \  
$KIBANA_HOME/bin/kibana plugin --install elastic/sense && \  
  
# Cleanup.  
rm -rf /tmp/* /var/cache/apk/* && apk del curl  
  
# Copy our config file and our entry point - the latter allows us to configure
our ES URL.  
COPY config $KIBANA_HOME/config  
COPY docker-entrypoint.sh /  
  
# Expose the ports we care about  
EXPOSE 5601  
# Get ready to run  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["kibana"]  

