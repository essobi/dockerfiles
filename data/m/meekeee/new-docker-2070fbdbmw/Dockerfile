#  
# Updated Docker image for the course 2070fbdbmw - Computational Neuroscience  
#  
# Sep 23rd 2017 - Antwerpen  
# Sep 19th 2017 - Antwerpen  
# July 13th 2017 - Antwerpen  
# October 8th 2016 - Antwerpen  
#  
# Michele Giugliano "plays" with Python, Julia, Jupyter Notebook, and Neuron
7.5 !  
#  
# Note: Julia version 0.6.0 is installed explicitly and  
# a .jl configuration script is then invoked  
# The python installation is made explicit (installing Anaconda) and Julia is  
# prevented from installing its own miniconda python dist.  
#  
# Distributed under the terms of the Modified BSD License.  
#  
# Compiled invoking: docker build -t new-docker-2070fbdbmw .  
# (or from an automated building in the cloud, through hub.docker.com and
https://bitbucket.org/mgiugliano/new-docker-2070fbdbmw)  
#  
# Simply launch it via > docker run -p 8888:8888 -v ~/Desktop:/opt/notebooks
docker-2070fbdbmw  
# (note the password for the jupyter botebook local server, available on the
host at http://localhost:8888 is mg)  
#  
# Adapted from the Docker files of continuumio/anaconda3, julia  
# Thank you Michael Hines, Andrew Davison, Christophe Verbist  
#  
#FROM debian:stretch-slim Neuron does NOT like the latest gcc, libs, etc.  
FROM debian:jessie-slim  
# Let's resort to the Debian 8 (latest, slim version)  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing \  
&& apt-get install -y --no-install-recommends ca-certificates build-essential\  
&& apt-get install -y wget curl bzip2 libncurses5-dev libx11-dev libxtst-dev
grep sed dpkg\  
&& apt-get install -y libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial
subversion \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh -O
~/anaconda.sh \  
&& /bin/bash ~/anaconda.sh -b -p /opt/conda \  
&& rm ~/anaconda.sh \  
&& /opt/conda/bin/conda install jupyter -y --quiet \  
&& mkdir /opt/notebooks  
  
RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep
-o "/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` \  
&& curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb \  
&& dpkg -i tini.deb \  
&& rm tini.deb \  
&& apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
ENV JULIA_PATH /opt/julia  
ENV JULIA_VERSION 0.6.0  
RUN mkdir $JULIA_PATH \  
&& curl -sSL
"https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
-o julia.tar.gz \  
# && curl -sSL
"https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz.asc"
-o julia.tar.gz.asc \  
# && export GNUPGHOME="$(mktemp -d)" \  
## http://julialang.org/juliareleases.asc  
## Julia (Binary signing key) <buildbot@julialang.org>  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
3673DF529D9049477F76B37566E3C7DC03D6E495 \  
# && gpg --batch --verify julia.tar.gz.asc julia.tar.gz \  
# && rm -r "$GNUPGHOME" julia.tar.gz.asc \  
&& tar -xzf julia.tar.gz -C $JULIA_PATH --strip-components 1 \  
&& rm -rf /var/lib/apt/lists/* julia.tar.gz*  
  
ENV PATH $JULIA_PATH/bin:$PATH  
  
RUN apt-get update \  
&& apt-get install -y unzip libxt6  
  
COPY julia_init.jl /tmp/  
RUN julia /tmp/julia_init.jl  
  
#RUN curl -sSL
"http://www.neuron.yale.edu/ftp/neuron/versions/v7.5/iv-19.tar.gz" -o
/opt/iv-19.tar.gz \  
# && cd /opt \  
# && tar -xf iv-19.tar.gz \  
# && mkdir iv \  
# && rm iv-19.tar.gz \  
# && cd /opt/iv-19 \  
# && ./configure --prefix=/opt/iv \  
# && make \  
# && make install  
RUN curl -sSL
"http://www.neuron.yale.edu/ftp/neuron/versions/v7.5/nrn-7.5.tar.gz" -o
/opt/nrn-7.5.tar.gz \  
&& cd /opt \  
&& tar -xf nrn-7.5.tar.gz \  
&& mkdir nrn \  
&& rm nrn-7.5.tar.gz \  
&& cd /opt/nrn-7.5 \  
&& ./configure --prefix=/opt/nrn --without-iv --with-nrnpython=dynamic --with-
pyexe=python3.6 \  
# && ./configure --prefix=/opt/nrn --with-iv=/opt/iv \  
# add also the following ?? --disable-rx3d --with-nrnpython-only \  
&& make \  
&& make install \  
&& cd src/nrnpython \  
&& /opt/conda/bin/python setup.py install  
  
ENV NRNHOME /opt/nrn  
# ENV IVHOME /opt/iv  
ENV CPU x86_64  
# ENV PATH $IVHOME/$CPU/bin:$PATH  
ENV PATH $NRNHOME/$CPU/bin:$PATH  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
EXPOSE 8888  
VOLUME /opt/notebooks  
WORKDIR /opt/notebooks  
  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--
allow-root", "--NotebookApp.token='mg'", "--notebook-dir=/opt/notebooks"]  
  

