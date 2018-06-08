FROM buildpack-deps:jessie  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
  
# Configure environment  
ENV DEBIAN_FRONTEND noninteractive  
ENV NB_USER mdp  
ENV NB_UID 1000  
ENV SHELL /bin/bash  
ENV HOME /home/$NB_USER  
ENV DATA_DIR /data  
ENV WORK_DIR /src  
ENV LANG C.UTF-8  
ENV PYTHON3_VERSION python3.4  
ENV PYTHON2_VERSION python2.7  
#useful basic packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
git \  
vim \  
jed \  
emacs \  
nano \  
wget \  
cmake \  
rsync \  
locales \  
software-properties-common \  
unzip \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
$PYTHON3_VERSION \  
$PYTHON2_VERSION \  
python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create NB_UID user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER \  
&& mkdir -p $WORK_DIR $DATA_DIR \  
&& chown $NB_USER $HOME $WORK_DIR $DATA_DIR \  
&& ln -s $WORK_DIR $HOME$WORK_DIR \  
&& ln -s $DATA_DIR $HOME$DATA_DIR  
  
VOLUME ["$WORK_DIR"]  
VOLUME ["$DATA_DIR"]  
  
USER $NB_USER  
WORKDIR $WORK_DIR  
  
CMD ["bash"]  

