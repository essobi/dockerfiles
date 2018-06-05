FROM fedora:25  
MAINTAINER Tristan CAREL <tristan.carel@epfl.ch>  
  
RUN echo 'check-update' \  
; dnf check-update -yv \  
; echo 'distro-sync' \  
; dnf distro-sync -yv \  
; echo 'install C Dev Tools' \  
; dnf group install -yv 'C Development Tools and Libraries' \  
&& echo 'install Dev tools' \  
&& dnf group install -yv 'Development Tools' \  
&& dnf install -y \  
bzip2 \  
bzip2-devel \  
cmake \  
fftw-devel \  
fftw-libs \  
graphviz \  
hdf5 \  
hdf5-devel \  
hostname \  
libgomp \  
libSM \  
libXext \  
libXrender \  
ncurses \  
ncurses-devel \  
ncurses-libs \  
pandoc \  
readline \  
readline-devel \  
wget  
  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
dnf -y install dpkg gnupg; \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /tmp/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /tmp/gosu.asc /usr/bin/gosu; \  
rm -r "$GNUPGHOME" /tmp/gosu.asc; \  
chmod +x /usr/bin/gosu; \  
gosu nobody true; \  
dnf -y remove dpkg gnupg; \  
dnf clean all  
  
ARG MINICONDA_VERSION=2-4.3.21  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet
https://repo.continuum.io/miniconda/Miniconda${MINICONDA_VERSION}-Linux-x86_64.sh
-O ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh \  
&& /opt/conda/bin/pip install jupyterlab matplotlib  
  
ENV PATH "/opt/conda/bin:$PATH"  
# Install Neuron  
RUN git clone https://github.com/nrnhines/nrn.git /opt/src/nrn \  
&& cd /opt/src/nrn \  
&& git checkout ee80eb94d3f34e86299a0498b5c1b87f8e8bcaa3 \  
&& cd /opt/src/nrn \  
&& ./build.sh \  
&& ./configure \  
\--prefix /opt/nrn \  
\--with-nrnpython=/opt/conda/bin/python \  
\--without-iv \  
&& make \  
&& make install  
  
ENV PYTHONPATH /opt/nrn/lib/python  
ENV PATH "/opt/nrn/x86_64/bin:$PATH"  
ENV LANG en_US.utf8  
  
ADD entrypoint /usr/bin/  
ENTRYPOINT ["/usr/bin/entrypoint"]  
  
CMD [ \  
"jupyter", "lab", \  
"--no-browser", "--allow-root", \  
"--notebook-dir=/opt/src/notebooks" \  
]  
  

