FROM ubuntu:xenial  
MAINTAINER Heiko Bornholdt "heiko@bornholdt.it"  
# Füge multiverse hinzu, da wir sonst kein unrar installieren können  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list.d/multiverse.list \  
&& \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list.d/multiverse.list \  
&& \  
echo "deb http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse" >>
/etc/apt/sources.list.d/multiverse.list \  
&& \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates multiverse" >>
/etc/apt/sources.list.d/multiverse.list \  
&& \  
echo "deb http://security.ubuntu.com/ubuntu xenial-security multiverse" >>
/etc/apt/sources.list.d/multiverse.list \  
&& \  
echo "deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse" >>
/etc/apt/sources.list.d/multiverse.list  
  
RUN apt-get update \  
&& \  
apt-get install -y \  
gettext-base \  
git \  
python-crypto \  
python-imaging \  
python-openssl \  
python-pycurl \  
python-qt4 \  
tesseract-ocr \  
gocr \  
python-django \  
openssl \  
unrar \  
rhino \  
locales \  
&& \  
locale-gen en_US.UTF-8 \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN git clone -b stable https://github.com/pyload/pyload.git /usr/share/pyload
\  
&& \  
rm -r /usr/share/pyload/.git \  
&& \  
ln -s /usr/share/pyload/pyLoadCore.py /usr/local/bin/pyLoadCore \  
&& \  
ln -s /usr/share/pyload/pyLoadCli.py /usr/local/bin/pyLoadCli \  
&& \  
ln -s /usr/share/pyload/pyLoadGui.py /usr/local/bin/pyLoadGui \  
&& \  
mkdir /etc/pyload \  
&& \  
echo "/etc/pyload" > /usr/share/pyload/module/config/configdir  
  
WORKDIR /usr/share/pyload  
  
# set file_log to False (we use docker logging)  
COPY default.conf /default.conf  
  
# Webinterface  
EXPOSE 8000  
# API (https://github.com/pyload/pyload/wiki/How-to-access-the-API)  
EXPOSE 7227  
# ClickNLoad  
EXPOSE 9666  
VOLUME /etc/pyload  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

