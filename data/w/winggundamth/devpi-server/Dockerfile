# devpi server  
#  
# PyPI server and packaging/testing/release tool  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install curl and python  
# 2) Install pip latest version  
# 3) Install devpi-server and devpi-web with pip  
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
apt-get install -y curl python && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install devpi-server devpi-web && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy /root/.cache  
  
CMD ["devpi-server", "--serverdir", "/var/lib/devpi/server", "--host", \  
"0.0.0.0"]  
EXPOSE 3141  
VOLUME ["/var/log", "/var/lib/devpi/server"]  

