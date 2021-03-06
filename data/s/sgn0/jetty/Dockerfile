FROM sgn0/java  
MAINTAINER Jesus Lopez, jesus@sgn.com  
  
# From jetty:9.3-jre8  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S jetty && adduser -S -G jetty jetty  
  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
RUN mkdir -p "$JETTY_HOME"  
WORKDIR $JETTY_HOME  
  
ENV JETTY_VERSION 9.3.8.v20160314  
ENV JETTY_TGZ_URL https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/$JETTY_VERSION/jetty-distribution-$JETTY_VERSION.tar.gz  
  
# GPG Keys are personal keys of Jetty committers (see
https://dev.eclipse.org/mhonarc/lists/jetty-users/msg05220.html)  
ENV JETTY_GPG_KEYS \  
# 1024D/8FB67BAC 2006-12-10 Joakim Erdfelt <joakime@apache.org>  
B59B67FD7904984367F931800818D9D68FB67BAC \  
# 1024D/D7C58886 2010-03-09 Jesse McConnell (signing key)
<jesse.mcconnell@gmail.com>  
5DE533CB43DAF8BC3E372283E7AE839CD7C58886  
RUN set -xe \  
&& apk --no-cache -t .downloadDeps add \  
curl \  
gnupg1 \  
tar \  
&& curl -sfSL "$JETTY_TGZ_URL" -o jetty.tar.gz \  
&& curl -sfSL "$JETTY_TGZ_URL.asc" -o jetty.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in $JETTY_GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; done \  
&& gpg --batch --verify jetty.tar.gz.asc jetty.tar.gz \  
&& rm -r "$GNUPGHOME" \  
&& tar -xvf jetty.tar.gz --strip-components=1 \  
&& sed -i '/jetty-logging/d' etc/jetty.conf \  
&& rm -fr demo-base javadoc \  
&& rm jetty.tar.gz* \  
&& chown -R jetty:jetty . \  
&& apk del --no-cache .downloadDeps  
  
ENV JETTY_BASE /var/lib/jetty  
WORKDIR $JETTY_BASE  
  
# Get the list of modules in the default start.ini and build new base with
those modules, then add setuid  
RUN modules="$(grep -- ^--module= "$JETTY_HOME/start.ini" | cut -d= -f2 |
xargs | sed 's/ /,/g')" \  
&& set -xe \  
&& java -jar "$JETTY_HOME/start.jar" \--add-to-startd="$modules,setuid" \  
&& chown -R jetty:jetty .  
  
ENV JETTY_RUN /run/jetty  
ENV JETTY_STATE $JETTY_RUN/jetty.state  
ENV TMPDIR /tmp/jetty  
RUN set -xe \  
&& mkdir -p "$JETTY_RUN" "$TMPDIR" \  
&& chown -R jetty:jetty "$JETTY_RUN" "$TMPDIR"  
  
COPY jetty /usr/bin/jetty  
  
EXPOSE 8080  
WORKDIR /  
CMD ["/usr/bin/jetty"]  

