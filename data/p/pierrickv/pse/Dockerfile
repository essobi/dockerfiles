FROM debian:stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV EMPIRE_VERSION 2.3  
ENV STAGING_KEY RANDOM  
  
RUN apt update -qq && apt install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
default-jdk \  
python-pip \  
python-dev \  
python-m2crypto \  
tar \  
lsb-release \  
libcrypto++-dev \  
libz-dev \  
libxml2-dev \  
libssl1.0-dev \  
swig \  
git \  
wget \  
&& wget -nv
https://github.com/EmpireProject/Empire/archive/$EMPIRE_VERSION.tar.gz
--output-document /empire.tar.gz \  
&& mkdir -p /empire \  
&& tar zxf empire.tar.gz -C /empire --strip-components=1 \  
&& cd /empire/setup/ && ./install.sh \  
&& chmod +x /empire/empire \  
&& rm /empire.tar.gz \  
&& apt autoremove -y \  
apt-transport-https \  
build-essential \  
git \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /empire  
ENTRYPOINT ["./empire"]  

