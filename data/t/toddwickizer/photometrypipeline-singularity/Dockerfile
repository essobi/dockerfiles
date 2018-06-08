FROM ubuntu:16.04  
# Maintainer: Todd Wickizer  
ENV PHOTPIPEDIR /usr/local/pipsrc  
ENV PIPEGITADDRESS https://github.com/mommermi/photometrypipeline.git  
ENV PYTHONPATH $PYTHONPATH:$PHOTPIPEDIR  
ENV PATH $PATH:$PHOTPIPEDIR  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's#http://archive.ubuntu.com/#http://tw.archive.ubuntu.com/#'
/etc/apt/sources.list  
  
# Install packages for VNC  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common curl
\  
&& sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >>
/etc/apt/sources.list.d/arc-theme.list" \  
&& curl -SL
http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
| apt-key add - \  
&& add-apt-repository ppa:fcwu-tw/ppa \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --allow-unauthenticated \  
supervisor \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
lxde x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
libreoffice firefox \  
fonts-wqy-microhei \  
language-pack-zh-hant language-pack-gnome-zh-hant firefox-locale-zh-hant
libreoffice-l10n-zh-tw \  
nginx \  
python-pip python-dev build-essential \  
mesa-utils libgl1-mesa-dri \  
gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme
\  
dbus-x11 x11-utils \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install packages for pipeline  
RUN apt-get update && apt-get install -y \  
build-essential \  
libssl-dev \  
libffi-dev \  
python-dev \  
git \  
python \  
sextractor \  
python-pip \  
wget \  
curl \  
libplplot-dev \  
libshp-dev \  
libcurl4-gnutls-dev \  
liblapack3 liblapack-dev liblapacke liblapacke-dev \  
libfftw3-3 libfftw3-dev libfftw3-single3 \  
libatlas-base-dev  
  
# Create the path  
RUN mkdir -p $PHOTPIPEDIR  
RUN cd $PHOTPIPEDIR \  
&& git clone "$PIPEGITADDRESS" .  
  
RUN pip install --upgrade pip  
RUN pip install numpy  
RUN pip install scipy  
RUN pip install astropy  
RUN pip install matplotlib  
RUN pip install callhorizons  
RUN pip install Pillow  
RUN pip install future  
RUN pip install cryptography  
RUN pip install astroquery  
  
# tini for subreap  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
  
# Now we install scamp  
WORKDIR $PHOTPIPEDIR  
  
RUN wget https://cdn.rawgit.com/towicode/towicode.github.io/8d4d8670/scamp-
trunk.r345.tar.gz  
RUN gzip -dc scamp-* | tar xvf -  
RUN cd trunk.r345 && ./configure --enable-threads && make && make install  
  
ADD image /  
RUN pip install setuptools wheel && pip install -r
/usr/lib/web/requirements.txt  
  
EXPOSE 80  
WORKDIR /root  
ENV HOME=/home/ubuntu \  
SHELL=/bin/bash  
  
RUN chmod +x /startup.sh  
RUN find /usr/lib/ -type f ! -name "*.c" -exec chmod +x {} +  
ENTRYPOINT ["/startup.sh"]  

