#name of container: docker-ijulia-notebook  
#versison of container: 0.5.8  
FROM quantumobject/docker-baseimage:16.04  
MAINTAINER Angel Rodriguez "angel@quantumobject.com"  
# Update the container  
# Installation of nesesary package/software for this containers...  
RUN echo "deb http://ppa.launchpad.net/staticfloat/juliareleases/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME` main " >> /etc/apt/sources.list \  
&& echo "deb http://ppa.launchpad.net/staticfloat/julia-deps/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME` main" >> /etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3D3D3ACC  
RUN apt-get update && apt-get install -y -q --no-install-recommends apt-utils
\  
git \  
build-essential \  
bzip2 \  
unzip \  
libcairo2-dev libpango1.0-0 libpango1.0-dev zlib1g-dev tk-dev tcl-dev \  
glib2.0 \  
file \  
python3 \  
python3-dev \  
file \  
ca-certificates \  
libsm6 \  
pandoc \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
libxrender1 \  
gfortran \  
gcc \  
fonts-dejavu \  
julia \  
libpng12-dev \  
libglib2.0-dev \  
librsvg2-dev \  
libpixman-1-dev \  
hdf5-tools \  
glpk-utils \  
libnlopt0 \  
imagemagick \  
inkscape \  
gettext \  
libreadline-dev \  
libncurses-dev \  
libpcre3-dev \  
libgnutls28-dev \  
tmux \  
pkg-config \  
pdf2svg \  
libc6 \  
libc6-dev \  
python-distribute \  
python3-software-properties \  
software-properties-common \  
python3-setuptools \  
python3-yaml \  
python-m2crypto \  
python-poppler \  
python3-crypto \  
python3-msgpack \  
libffi-dev \  
libssl-dev \  
libzmq3-dev \  
python3-pip \  
python3-zmq \  
python3-jinja2 \  
python3-requests \  
python3-numpy \  
python3-isodate \  
libsundials-cvode1 \  
libsundials-cvodes2 \  
libsundials-ida2 \  
libsundials-idas0 \  
libsundials-kinsol1 \  
libsundials-nvecserial0 \  
libsundials-serial \  
libsundials-serial-dev \  
libnlopt-dev \  
openmpi-bin \  
libopenmpi-dev \  
libblosc-dev \  
libavcodec-ffmpeg56 libavdevice-ffmpeg56 libavfilter-ffmpeg5 \  
libavformat-ffmpeg56 libavutil-ffmpeg54 libswscale-ffmpeg3 libavresample-
ffmpeg2 \  
libgmp-dev libglpk-dev \  
libmumps-dev \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV CONDA_JL_HOME $CONDA_DIR/conda_jl  
ENV SHELL /bin/bash  
  
##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
##Adding Deamons to containers  
RUN mkdir /etc/service/ijulia  
COPY ijulia.sh /etc/service/ijulia/run  
RUN chmod +x /etc/service/ijulia/run  
  
#pre-config scritp for different service that need to be run when container
image is create  
#maybe include additional software that need to be installed ... with some
service running ... like example mysqld  
COPY pre-conf.sh /sbin/pre-conf  
RUN chmod +x /sbin/pre-conf ; sync \  
&& /bin/bash -c /sbin/pre-conf \  
&& rm /sbin/pre-conf  
  
#add files and script that need to be use for this container  
#include conf file relate to service/daemon  
#additionsl tools to be use internally  
COPY after_install.sh /sbin/after_install  
RUN chmod +x /sbin/after_install  
  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 8998  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

