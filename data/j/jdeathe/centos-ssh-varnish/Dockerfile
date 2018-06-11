#
=============================================================================  
# jdeathe/centos-ssh-varnish  
#  
# CentOS-6, Varnish 4.1  
#  
#
=============================================================================  
FROM jdeathe/centos-ssh:1.8.4  
#
-----------------------------------------------------------------------------  
# Install Varnish Cache  
#
-----------------------------------------------------------------------------  
RUN rpm --rebuilddb \  
&& rpm -iv
https://packagecloud.io/varnishcache/varnish41/packages/el/6/varnish-
release-4.1-4.el6.noarch.rpm/download \  
&& yum -y install \  
\--setopt=tsflags=nodocs \  
\--disableplugin=fastestmirror \  
gcc-4.4.7-18.el6 \  
varnish-4.1.10-1.el6 \  
&& yum versionlock add \  
varnish \  
gcc \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
#
-----------------------------------------------------------------------------  
# Copy files into place  
#
-----------------------------------------------------------------------------  
ADD src/usr/bin \  
/usr/bin/  
ADD src/usr/sbin \  
/usr/sbin/  
ADD src/opt/scmi \  
/opt/scmi/  
ADD src/etc/services-config/supervisor/supervisord.d \  
/etc/services-config/supervisor/supervisord.d/  
ADD src/etc/services-config/varnish/docker-default.vcl \  
/etc/services-config/varnish/  
ADD src/etc/systemd/system \  
/etc/systemd/system/  
  
RUN ln -sf \  
/etc/services-config/supervisor/supervisord.d/varnishd-wrapper.conf \  
/etc/supervisord.d/varnishd-wrapper.conf \  
&& ln -sf \  
/etc/services-config/varnish/docker-default.vcl \  
/etc/varnish/docker-default.vcl \  
&& chmod 644 \  
/etc/varnish/*.vcl \  
&& chmod 700 \  
/usr/{bin/healthcheck,sbin/varnishd-wrapper}  
  
EXPOSE 80 8443  
#
-----------------------------------------------------------------------------  
# Set default environment variables  
#
-----------------------------------------------------------------------------  
ENV SSH_AUTOSTART_SSHD=false \  
SSH_AUTOSTART_SSHD_BOOTSTRAP=false \  
VARNISH_MAX_THREADS="1000" \  
VARNISH_MIN_THREADS="50" \  
VARNISH_STORAGE="file,/var/lib/varnish/varnish_storage.bin,1G" \  
VARNISH_THREAD_TIMEOUT="120" \  
VARNISH_TTL="120" \  
VARNISH_VCL_CONF="/etc/varnish/docker-default.vcl"  
#
-----------------------------------------------------------------------------  
# Set image metadata  
#
-----------------------------------------------------------------------------  
ARG RELEASE_VERSION="1.4.3"  
LABEL \  
maintainer="James Deathe <james.deathe@gmail.com>" \  
install="docker run \  
\--rm \  
\--privileged \  
\--volume /:/media/root \  
jdeathe/centos-ssh-varnish:${RELEASE_VERSION} \  
/usr/sbin/scmi install \  
\--chroot=/media/root \  
\--name=\${NAME} \  
\--tag=${RELEASE_VERSION}" \  
uninstall="docker run \  
\--rm \  
\--privileged \  
\--volume /:/media/root \  
jdeathe/centos-ssh-varnish:${RELEASE_VERSION} \  
/usr/sbin/scmi uninstall \  
\--chroot=/media/root \  
\--name=\${NAME} \  
\--tag=${RELEASE_VERSION}" \  
org.deathe.name="centos-ssh-varnish" \  
org.deathe.version="${RELEASE_VERSION}" \  
org.deathe.release="jdeathe/centos-ssh-varnish:${RELEASE_VERSION}" \  
org.deathe.license="MIT" \  
org.deathe.vendor="jdeathe" \  
org.deathe.url="https://github.com/jdeathe/centos-ssh-varnish" \  
org.deathe.description="CentOS-6 6.9 x86_64 - Varnish Cache 4.1."  
  
HEALTHCHECK \  
\--interval=0.5s \  
\--timeout=1s \  
\--retries=4 \  
CMD ["/usr/bin/healthcheck"]  
  
CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]

