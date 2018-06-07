FROM phusion/baseimage  
MAINTAINER Zac Heacker <zac.heacker@gmail.com>  
  
# phusion baseimage with my_init  
# install atom  
# install anaconda  
# install hydrogen pre-reqs  
# install hydrogen  
# setup hydrogen with anaconda kernel  
# phusion baseimage init  
CMD ["/sbin/my_init"]  
  
  
# environment variables  
# for atom  
ENV ATOM_VERSION=1.12.5 \  
# for anaconda  
LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
# install dependencies  
RUN apt-get update && apt-get install -y \  
# for atom  
ca-certificates \  
curl \  
git \  
gconf2 \  
gconf-service \  
gvfs-bin \  
libasound2 \  
libcap2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
xdg-utils \  
# for anaconda  
bzip2 \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxrender1 \  
# for hydrogen  
g++ \  
gcc \  
make \  
  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# install atom/anaconda/hydrogen  
# atom  
RUN set -x \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sSL
https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-amd64.deb
-o /tmp/atom-amd64.deb \  
&& dpkg -i /tmp/atom-amd64.deb \  
&& rm -rf /tmp/*.deb \  
# anaconda (v3)  
&& echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& curl -sSL https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
-o /tmp/anaconda.sh \  
&& /bin/bash /tmp/anaconda.sh -b -p /opt/conda \  
&& rm /tmp/anaconda.sh \  
# hydrogen  
&& PYTHON=python2.7 apm install hydrogen \  
# final cleanup - from phusion/baseimage  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# not sure if I should get rid of these packages...  
# && apt-get purge -y --auto-remove ca-certificates curl \  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT [ "atom", "--foreground" ]  

