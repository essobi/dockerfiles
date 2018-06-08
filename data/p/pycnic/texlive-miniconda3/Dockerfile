FROM pycnic/texlive:latest  
  
MAINTAINER Andreas Sorge <as@pycnic.org>  
  
# See https://github.com/ContinuumIO/docker-
images/blob/4dd61cf7676be7ea791ae482306a68bcccb51eb2/miniconda3/Dockerfile  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
  
RUN apt-get update \--fix-missing \  
&& apt-get install -y \--no-install-recommends wget bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT ["/usr/bin/tini", "--"]  
CMD ["/bin/bash"]  

