# Dockerfile  
FROM debian:stretch  
  
RUN sed -i "s/httpredir/ftp.fr/" /etc/apt/sources.list  
  
RUN apt-get clean && apt-get update && apt-get install -y \  
gnupg \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb http://www.yade-dem.org/packages/ stretch/" >>
/etc/apt/sources.list  
  
RUN wget -O - http://www.yade-dem.org/packages/yadedev_pub.gpg | apt-key add -  
RUN apt-get clean && apt-get update && \  
apt-get install -y x11vnc unzip xvfb iceweasel fluxbox net-tools vim \  
build-essential \  
cmake \  
devscripts \  
dpkg-dev \  
dvipng \  
fakeroot \  
freeglut3-dev \  
g++ \  
git \  
git-buildpackage \  
gnuplot \  
gtk2-engines-pixbuf \  
help2man \  
ipython \  
libboost-all-dev \  
libbz2-dev \  
libcgal-dev \  
libeigen3-dev \  
libgts-dev \  
libjs-jquery \  
libloki-dev \  
libmetis-dev \  
libopenblas-dev \  
libqglviewer-dev-qt5 \  
libqglviewer-headers \  
libsqlite3-dev \  
libsuitesparse-dev \  
libvtk6-dev \  
libxi-dev \  
libxmu-dev \  
lmodern \  
pyqt5-dev-tools \  
pyqt5-dev-tools \  
python-all-dev \  
python-argparse \  
python-bibtex \  
python-dev \  
python-git \  
python-gts \  
python-imaging \  
python-matplotlib \  
python-minieigen \  
python-numpy \  
python-numpy \  
python-pygraphviz \  
python-pyqt5 \  
python-pyqt5.qtwebkit \  
python-sphinx \  
python-tk \  
python-xlib \  
texlive-fonts-recommended \  
texlive-generic-extra \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-pictures \  
texlive-xetex \  
tipa \  
zlib1g-dev  
  
RUN apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
COPY startup /usr/local/bin/  
  
CMD startup  
  
EXPOSE 5900  

