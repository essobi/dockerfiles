FROM alpine:latest  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
ARG SABNZBD_VERSION=2.3.3  
ARG
SABNZBD_URL=https://github.com/sabnzbd/sabnzbd/releases/download/2.3.3/SABnzbd-2.3.3-src.tar.gz  
ARG YENC_VERSION=0.4.0  
ENV \  
HOME=/config \  
TEST=1  
RUN \  
apk add --update gcc autoconf automake curl git g++ make python-dev openssl-
dev libffi-dev && \  
git clone https://github.com/Parchive/par2cmdline /root/par2cmdline && \  
cd /root/par2cmdline && \  
aclocal && automake --add-missing && autoconf && ./configure && make && make
install && \  
apk add unrar unzip p7zip py-pip openssl libffi && \  
pip install cheetah configobj feedparser pyOpenSSL sabyenc && \  
curl "http://www.golug.it/pub/yenc/yenc-${YENC_VERSION}.tar.gz" -o
"/root/yenc-${YENC_VERSION}.tar.gz" && \  
tar -C /root -zxf "/root/yenc-${YENC_VERSION}.tar.gz" && \  
cd "/root/yenc-${YENC_VERSION}" && \  
python setup.py build && python setup.py install && \  
apk del gcc autoconf automake git g++ make python-dev openssl-dev libffi-dev
&& \  
mkdir -p /opt/sabnzbd && \  
curl -L "${SABNZBD_URL}" -o "/root/sabnzbd-${SABNZBD_VERSION}.tar.gz" && \  
tar zxvf "/root/sabnzbd-${SABNZBD_VERSION}.tar.gz" \--strip 1 -C /opt/sabnzbd/
&& \  
rm -rf /var/cache/apk/* /root/par2cmdline /root/pip.py
"/root/yenc-${YENC_VERSION}.tar.gz" "/root/yenc-${YENC_VERSION}"  
  
# Latest unstable release  
# curl -L \  
# $(curl -s \  
# https://api.github.com/repos/sabnzbd/sabnzbd/releases/latest \  
# | jq -r ".assets[] | select(.name | test(\"Jackett.Binaries.Mono.tar.gz\"))
| .browser_download_url" \  
# ) \  
# -o /tmp/Sabnzbd.tar.gz && \  
# Latest stable release  
# URL=$(curl -s \  
# https://api.github.com/repos/sabnzbd/sabnzbd/releases \  
# | jq -r "[ .[] | .assets[] | select(.name |
test(\"SABnzbd-[0-9.]+-src.tar.gz\")) ] | first | .browser_download_url")  
# Version X  
# curl https://api.github.com/repos/sabnzbd/sabnzbd/releases | jq -r " .[] |
.assets[] | select(.name | test(\"SABnzbd-${SABNZBD_VERSION}-src.tar.gz\")) |
.browser_download_url"  
EXPOSE 8080  
VOLUME ["/config", "/downloads"]  
  
ENTRYPOINT [ "/usr/bin/python", "/opt/sabnzbd/SABnzbd.py", "-f",
"/config/sabnzbd.ini", "-s", "0.0.0.0:8080", "-b", "0" ]  

