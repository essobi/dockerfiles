FROM minimum2scp/baseimage-jessie:latest  
  
MAINTAINER YAMADA Tsuyoshi <tyamada@minimum2scp.org>  
  
ARG NGINX_VERSION=1.11.4  
ARG NGX_MRUBY_VERSION=v1.18.6  
ARG DEB_BASE_REVISION=1~jessie  
ARG DEB_NGINX_MODULE_MRUBY_VERSION=${NGINX_VERSION}-${NGX_MRUBY_VERSION}  
  
RUN sed -i -e 's/httpredir.debian.org/ftp.jp.debian.org/'
/etc/apt/sources.list  
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN echo "deb-src http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list.d/nginx.list  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends fakeroot devscripts git patch
ruby rake bison  
RUN apt-get build-dep -y nginx=${NGINX_VERSION}-${DEB_BASE_REVISION}  
  
USER debian  
RUN mkdir /home/debian/build  
  
WORKDIR /home/debian/build  
RUN apt-get source nginx=${NGINX_VERSION}-${DEB_BASE_REVISION}  
  
WORKDIR /home/debian/build/nginx-${NGINX_VERSION}  
RUN git clone https://github.com/matsumoto-r/ngx_mruby.git
debian/extra/ngx_mruby/  
RUN cd debian/extra/ngx_mruby && git checkout ${NGX_MRUBY_VERSION}  
  
ADD rules.diff /tmp/rules.diff  
ADD control.diff /tmp/control.diff  
  
ADD nginx-module-mruby.install
/home/debian/build/nginx-${NGINX_VERSION}/debian/nginx-module-mruby.install  
ADD nginx-module-mruby.preinst
/home/debian/build/nginx-${NGINX_VERSION}/debian/nginx-module-mruby.preinst  
RUN echo "${DEB_NGINX_MODULE_MRUBY_VERSION}" >
/home/debian/build/nginx-${NGINX_VERSION}/debian/nginx-module-mruby.version  
  
RUN patch -p1 < /tmp/rules.diff  
RUN patch -p1 < /tmp/control.diff  
  
RUN debchange --local '+local' 'Added mruby dynamic modules subpackage'  
RUN debuild -rfakeroot -uc -us  
  
USER root  
WORKDIR /home/debian/build  
RUN dpkg -i nginx_${NGINX_VERSION}-${DEB_BASE_REVISION}+local1_amd64.deb
nginx-module-mruby_${DEB_NGINX_MODULE_MRUBY_VERSION}~`lsb_release
-cs`_amd64.deb  
RUN apt-get install -f -y --no-install-recommends  
  
ADD nginx-conf.diff /tmp/nginx-conf.diff  
RUN cd /etc; patch -p1 < /tmp/nginx-conf.diff && rm /tmp/nginx-conf.diff  
  
WORKDIR /  
EXPOSE 22 80  
ENTRYPOINT ["/opt/init-wrapper/sbin/entrypoint.sh"]  
CMD ["/sbin/init"]  
  

