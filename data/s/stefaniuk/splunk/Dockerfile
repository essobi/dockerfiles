FROM stefaniuk/ubuntu:16.04-20160905  
MAINTAINER daniel.stefaniuk@gmail.com  
# SEE: https://github.com/outcoldman/docker-
splunk/blob/master/splunk/Dockerfile  
ARG APT_PROXY  
ENV SPLUNK_VERSION="6.4.3" \  
SPLUNK_BUILD="b03109c2bad4" \  
SPLUNK_URL="https://download.splunk.com/products/splunk/releases" \  
SPLUNK_HOME=/opt/splunk \  
SPLUNK_PASSWORD="admin" \  
SPLUNK_DEFAULT_ETC=/etc/splunk \  
SPLUNK_USER_ETC=/usr/etc/splunk \  
PATH="$PATH:/opt/splunk/bin"  
RUN set -ex \  
\  
&& if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy \"$APT_PROXY\";
};" >> /etc/apt/apt.conf.d/00proxy; fi \  
&& apt-get --yes update \  
&& apt-get --yes install \  
libgssapi-krb5-2 \  
\  
&& file=splunk-$SPLUNK_VERSION-$SPLUNK_BUILD-Linux-x86_64.tgz \  
&& wget -O /tmp/$file $SPLUNK_URL/$SPLUNK_VERSION/linux/$file \  
&& wget -O /tmp/$file.md5 $SPLUNK_URL/$SPLUNK_VERSION/linux/$file.md5 \  
&& (cd /tmp && md5sum -c $file.md5) \  
&& mkdir -p $SPLUNK_HOME \  
&& tar xzf /tmp/$file \--strip 1 -C $SPLUNK_HOME \  
&& cp -R $SPLUNK_HOME/etc $SPLUNK_DEFAULT_ETC \  
\  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/* \  
&& rm -f /etc/apt/apt.conf.d/00proxy  
  
COPY assets/usr/etc/splunk /usr/etc/splunk  
ONBUILD COPY assets/usr/etc/splunk /usr/etc/splunk  
  
VOLUME [ "/opt/splunk/var" ]  
EXPOSE 1514 8000 8088 8089 8191 9997  
COPY assets/sbin/entrypoint.sh /sbin/entrypoint.sh  
  
### METADATA
###################################################################  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
version=$VERSION \  
build-date=$BUILD_DATE \  
vcs-ref=$VCS_REF \  
vcs-url=$VCS_URL \  
license="MIT"  

