FROM alpine:3.6  
  
MAINTAINER Frank Mai <frank@rancher.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
io.github.thxcode.build-date=$BUILD_DATE \  
io.github.thxcode.name="subversion" \  
io.github.thxcode.description="Subversion with Apache web server in a docker
container." \  
io.github.thxcode.url="https://github.com/thxcode/subversion" \  
io.github.thxcode.vcs-type="Git" \  
io.github.thxcode.vcs-ref=$VCS_REF \  
io.github.thxcode.vcs-url="https://github.com/thxcode/subversion.git" \  
io.github.thxcode.vendor="Rancher Labs, Inc" \  
io.github.thxcode.version=$VERSION \  
io.github.thxcode.schema-version="1.0" \  
io.github.thxcode.license="MIT" \  
io.github.thxcode.docker.dockerfile="/Dockerfile"  
  
ENV SVN_VERSION="1.9.7-r0" \  
SVN_AUTH_TYPE=Basic \  
SVN_AUTH_NAME="Subversion Repository" \  
SVN_ANONYMOUS_ACCESS=false  
  
COPY svn-* /usr/local/bin/  
  
RUN apk add --update --no-cache \  
dumb-init bash sudo \  
openssl jq curl \  
python python-dev py-pip \  
apache2 apache2-utils apache2-webdav apache2-proxy mod_dav_svn \  
"subversion=${SVN_VERSION}" \  
&& rm -fr /var/cache/apk/* \  
&& pip install passlib kubernetes==4.0.0b1 \  
&& adduser apache svnusers \  
&& mkdir -p /opt /run/apache2 \  
&& mv /etc/apache2/httpd.conf /etc/apache2/httpd.conf.bak \  
&& rm -f /etc/apache2/conf.d/dav.conf \  
&& rm -f /etc/apache2/conf.d/proxy.conf \  
&& rm -rf /var/svn \  
&& chmod +x /usr/local/bin/svn-*  
  
EXPOSE 80/tcp  
VOLUME ["/opt"]  
  
ENTRYPOINT ["svn-entrypoint"]  
CMD ["start"]

