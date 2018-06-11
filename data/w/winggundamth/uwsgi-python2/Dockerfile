# uWSGI with Python 2.7  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng (Dear) <jirayut.n@kaidee.com>  
ENV FROM_BASE=xenial-20160809  
# 1) Update and install python and required packages to compile library  
# 2) Install pip latest version  
# 3) Install uwsgi with pip  
# 4) Clean to reduce Docker image size  
ARG APT_CACHER_NG  
ARG DEVPI_SERVER  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
[ -n "$DEVPI_SERVER" ] && \  
mkdir -p ~/.pip && \  
echo "[global]\n\  
index-url = $DEVPI_SERVER\n\  
trusted-host = \  
$(echo $DEVPI_SERVER | awk -F/ '{print $3}' | awk -F: '{print $1}')\n\  
" >> ~/.pip/pip.conf || true; \  
apt-get update && \  
apt-get install -y curl python libpython2.7 python-dev build-essential && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install uwsgi && \  
apt-get remove --purge --auto-remove -y \  
build-essential ifupdown iproute2 isc-dhcp-client isc-dhcp-common \  
libatm1 libisc-export160 libmnl0 libxtables11 manpages netbase \  
curl python-dev && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /usr/lib/x86_64-linux-gnu/libfakeroot /var/lib/apt/lists/* \  
/etc/apt/apt.conf.d/11proxy /root/.cache /root/.pip  
  
CMD ["/start.py"]  
EXPOSE 5000  
# 1) Add user web and prepare .ssh directory  
# 2) Copy initial uwsgi ini file  
ENV WEB_USER=web  
ENV HOME=/home/$WEB_USER WEB_HOME=/home/$WEB_USER  
COPY build-files /build-files  
RUN useradd --shell /bin/bash --home-dir $WEB_HOME \--create-home \  
\--base-dir $WEB_HOME $WEB_USER && \  
mkdir -p $WEB_HOME/.ssh && \  
chmod 700 /$WEB_HOME/.ssh && \  
chown $WEB_USER:$WEB_USER $WEB_HOME/.ssh && \  
mv /build-files/uwsgi.ini /etc/uwsgi.ini && \  
mkdir -p /var/log/uwsgi && \  
rm -rf /build-files  
  
VOLUME ["/var/log"]  
WORKDIR $WEB_HOME  
USER $WEB_USER  
EXPOSE 5000  
ENTRYPOINT ["uwsgi"]  
CMD ["/etc/uwsgi.ini"]  

