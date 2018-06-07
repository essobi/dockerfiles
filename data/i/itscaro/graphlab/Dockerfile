FROM debian:jessie  
MAINTAINER Minh-Quan TRAN <account@itscaro.me>  
  
# Install some useful packages & OpenCV dependencies (taken from build  
# dependencies for Debian package).  
RUN apt-get -y update && apt-get -y install libgstreamer1.0-dev \  
libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev \  
libgtkglext1-dev libgl1-mesa-dev libglu1-mesa-dev libjasper-dev \  
libjpeg-dev libpng-dev libtiff-dev libopenexr-dev libraw1394-dev \  
libdc1394-22-dev libv4l-dev zlib1g-dev liblapack-dev libtbb-dev \  
libeigen3-dev ocl-icd-opencl-dev python-dev python-numpy python-sphinx \  
ant default-jdk javahelper texlive-fonts-extra texlive-latex-extra \  
texlive-latex-recommended latex-xcolor texlive-fonts-recommended \  
vim git htop python-dev python3-dev bash-completion cmake \  
libgstreamer-plugins-base1.0-dev gstreamer1.0-libav libavresample-dev \  
libavcodec-dev libavformat-dev libavutil-dev libswscale-dev \  
libavresample-dev libtbb-dev sudo python-pip python3-pip llvm-dev \  
python-numpy python3-numpy python-scipy python3-scipy python-pil \  
python3-pil python-enum34 python-matplotlib python3-matplotlib  
  
RUN apt-get update \--fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-3.19.0-Linux-x86_64.sh && \  
/bin/bash /Miniconda2-3.19.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda2-3.19.0-Linux-x86_64.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Copy local configuration & fix perms  
ADD system-conf /  
RUN chown -R root:root /etc/sudoers.d && chmod 0440 /etc/sudoers.d/*  
RUN addgroup compute-users  
  
# Run any system setup  
ADD setup /tmp/setup  
RUN cd /tmp/setup && ./setup-system.sh && rm -r /tmp/setup  
  
# GraphLab  
RUN conda create -n dato-env python=2.7 anaconda  
RUN /bin/bash -c "source activate dato-env && \  
conda update pip && \  
conda install ipython ipython-notebook"  
  
ENV [ GRAPHLAB_VERSION, "1.8.3", GRAPHLAB_EMAIL, "", GRAPHLAB_LICENSE, "" ]  
  
EXPOSE 8888  
ADD run.sh /opt/compute-container/run.sh  
CMD /opt/compute-container/run.sh  

