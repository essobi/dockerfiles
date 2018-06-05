FROM ubuntu:14.04  
MAINTAINER Alan Fachini <alfakini@gmail.com>  
  
RUN apt-get update --fix-missing && \  
apt-get install -y \  
build-essential \  
bzip2 \  
unzip \  
cmake \  
git \  
wget \  
curl \  
grep \  
sed \  
vim \  
gfortran \  
pkg-config \  
ca-certificates  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV ANACONDA_ROOT /opt/anaconda  
ENV PATH $ANACONDA_ROOT/bin:$PATH  
  
RUN wget https://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh -P
/tmp/  
RUN /bin/bash /tmp/Anaconda2-4.0.0-Linux-x86_64.sh -b -p $ANACONDA_ROOT  
  
WORKDIR /root  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
CMD [ "/bin/bash" ]  

