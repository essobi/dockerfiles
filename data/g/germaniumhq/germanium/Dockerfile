FROM ubuntu:16.04  
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>  
  
ENV REFRESHED_AT="2016.08.02-22:59:45"  
# allowed options are firefox, chrome.  
ENV TEST_BROWSER=firefox  
  
ENV PYTHON_VERSION=3.5.2  
ENV RUN_VNC_SERVER=1  
ENV VNC_SERVER_WIDTH=1024  
ENV VNC_SERVER_HEIGHT=768  
ENV VNC_SERVER_BPP=16  
ENV RUN_WEB_INTERFACE=0  
ENV RUN_ICEWM=1  
ENV VNC_PASSWORD=germanium  
  
ENV DISPLAY=:1  
ENV UID=1000  
ENV GID=1000  
EXPOSE 8081  
EXPOSE 5901  
# system update  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common  
  
#  
# Actual python installation required programs, and general dependencies.  
#  
RUN apt-get install -y \  
wget \  
libssl-dev \  
openssl \  
build-essential \  
unzip \  
bzip2  
  
RUN mkdir /build && \  
cd /build && \  
wget
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-${PYTHON_VERSION}.tgz
&& \  
tar -zxvf Python-${PYTHON_VERSION}.tgz && \  
cd Python-${PYTHON_VERSION} && \  
./configure && \  
make && \  
make install && \  
rm -fr /build  
  
ENV PYTHON_BINARY=/usr/local/bin/python3.5  
# Install behave and germanium into the package.  
RUN $PYTHON_BINARY -m ensurepip && \  
$PYTHON_BINARY -m pip install virtualenv && \  
virtualenv /python && \  
/python/bin/pip install behave  
  
#  
# Install remoting apps  
#  
RUN apt-get install -y vnc4server \  
parcellite \  
novnc \  
websockify \  
psmisc \  
icewm  
  
# Setup remoting  
RUN useradd -m germanium  
  
RUN cp -R /usr/share/novnc /home/germanium/novnc && \  
mkdir -p /home/germanium/.icewm && \  
echo 'Theme="metal2/default.theme"' > /home/germanium/.icewm/theme && \  
mkdir -p /home/germanium/.vnc  
  
COPY bin/docker/index.html /home/germanium/novnc/  
COPY bin/docker/xstartup /home/germanium/.vnc/xstartup  
  
#  
# BROWSERS SECTION  
#  
ENV BROWSERS_REFRESHED_AT="2016.08.08-00:11:03"  
#  
# Install firefox, and its webdriver  
#  
RUN cd /opt && \  
wget
'https://download.mozilla.org/?product=firefox-47.0.1-SSL&os=linux64&lang=en-
US' -O firefox.tar.bz2 && \  
tar -jxvf firefox.tar.bz2 && \  
rm /opt/firefox.tar.bz2  
  
ENV PATH /opt/firefox:$PATH  
  
#  
# install chrome, and its webdriver  
#  
RUN cd /tmp && \  
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
&& \  
dpkg -i google-chrome-stable_current_amd64.deb || apt-get -y -f install  
  
#  
# Behave run script  
#  
COPY bin/docker/run-behave.sh /home/germanium/bin/run-behave.sh  
  
# Allow configuring the Python Package Index location, to speed up builds,  
# and validate germaniumdrivers pacakge updates, before publishing them to  
# the real pypi.  
# PYPI repository location  
ARG pypi_url=https://pypi.python.org/  
# PYPI index location  
ARG pypi_index_url=https://pypi.python.org/simple  
  
# the funky looking regexp just extracts the hostname, excluding port  
# to be used as a trusted-host.  
RUN mkdir ~/.pip && \  
echo "[global]" > ~/.pip/pip.conf && \  
echo "index = $pypi_url" >> ~/.pip/pip.conf && \  
echo "index-url = $pypi_index_url" >> ~/.pip/pip.conf && \  
echo "trusted-host = $(echo $pypi_url | perl -pe
's|^.*?://(.*?)(:.*?)?/.*$|$1|')" >> ~/.pip/pip.conf  
  
COPY requirements.txt /root/requirements.txt  
RUN cd /root && \  
/python/bin/pip install -r requirements.txt && \  
rm /root/requirements.txt  
  
# add germanium the project only after having the docker binaries in the  
# home folder, to reduce the time to create new docker images  
COPY . /germanium  
RUN cd /germanium && \  
/python/bin/python setup.py install && \  
rm -fr /germanium  
  
RUN perl -pi -e "s/germanium:x:1000:1000/germanium:x:$UID:$GID/" /etc/passwd
&& \  
perl -pi -e "s/germanium:x:1000:/germanium:x:$GID:/" /etc/group && \  
chown -R germanium:germanium /home/germanium/ /python  
  
USER germanium  
  
CMD /home/germanium/bin/run-behave.sh  

