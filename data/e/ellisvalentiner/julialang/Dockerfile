# Ubuntu Docker file for Julia  
FROM ubuntu:16.04  
MAINTAINER Ellis Valentiner  
  
ENV VER=0.6.0  
RUN apt-get update \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o
DPkg::Options::="--force-confold" \  
&& apt-get install -y \  
man-db \  
libc6 \  
libc6-dev \  
build-essential \  
wget \  
curl \  
file \  
vim \  
screen \  
tmux \  
unzip \  
pkg-config \  
cmake \  
gfortran \  
gettext \  
libreadline-dev \  
libncurses-dev \  
libpcre3-dev \  
libgnutls30 \  
libzmq3-dev \  
libzmq5 \  
python \  
python-yaml \  
python-m2crypto \  
python-crypto \  
msgpack-python \  
python-dev \  
python-setuptools \  
supervisor \  
python-jinja2 \  
python-requests \  
python-isodate \  
python-git \  
python-pip \  
&& apt-get clean  
  
RUN pip install --upgrade pip pyzmq PyDrive google-api-python-client
jsonpointer jsonschema tornado sphinx pygments nose readline mistune invoke  
  
RUN pip install 'notebook==4.2'  
  
# Install julia  
RUN mkdir -p /opt/julia-${VER} && \  
curl -s -L https://julialang.s3.amazonaws.com/bin/linux/x64/`echo $VER | cut
-d "." -f 1,2`/julia-${VER}-linux-x86_64.tar.gz | tar -C /opt/julia-${VER} -x
-z --strip-components=1 -f -  
  
# Make verison default julia  
RUN ln -fs /opt/julia-${VER} /opt/julia  
  
RUN echo
"PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/julia/bin\""
> /etc/environment && \  
echo "export PATH" >> /etc/environment && \  
echo "source /etc/environment" >> /root/.bashrc  
  
RUN /opt/julia/bin/julia -e 'Pkg.add("IJulia")'  
RUN /opt/julia/bin/julia -e 'Pkg.build("IJulia")'  
  
ENTRYPOINT /bin/bash  

