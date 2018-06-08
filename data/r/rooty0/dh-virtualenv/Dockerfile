FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
DEB_BUILD_OPTIONS="nocheck nodocs"  
  
VOLUME "/build/src"  
# Disable documentation installation  
RUN echo 'path-exclude=/usr/share/doc/*' > /etc/dpkg/dpkg.cfg.d/01-no_docs \  
&& echo 'path-exclude=/usr/share/info/*' >> /etc/dpkg/dpkg.cfg.d/01-no_docs \  
&& echo 'path-exclude=/usr/share/locale/*' >> /etc/dpkg/dpkg.cfg.d/01-no_docs
\  
&& echo 'path-exclude=/usr/share/man/*' >> /etc/dpkg/dpkg.cfg.d/01-no_docs  
  
# Build dependencies  
RUN apt-get update \  
&& apt-get install -yy --no-install-recommends \  
ca-certificates \  
curl \  
less \  
devscripts \  
equivs \  
gcc \  
git \  
libfile-fcntllock-perl \  
python-dev \  
python-virtualenv \  
virtualenv \  
reprepro \  
&& git clone https://github.com/spotify/dh-virtualenv.git -b 1.0 \  
&& cd dh-virtualenv \  
&& mk-build-deps -t 'apt-get -yy' -ri \  
&& dpkg-buildpackage -us -uc -b \  
&& dpkg -i ../dh-virtualenv_*.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /dh-virtualen*  

