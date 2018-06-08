FROM ubuntu:latest  
  
RUN apt-get update -q && apt-get install -yq --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
mono-complete \  
python3 \  
python3-pip \  
python3-setuptools \  
wget \  
zip \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -yq nodejs --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
# Install gitsemver  
ADD http://downloads.haprotec.de/gitsemver/gitsemver.deb /  
RUN dpkg -i ./gitsemver.deb && rm gitsemver.deb  
  
# Add haprotec Python library  
RUN cd /usr/local/lib && \  
git clone https://gitlab.com/haprotec/haprotec-python-lib.git && \  
pip3 install -e ./haprotec-python-lib && \  
cd /  
  
# Install create-deb-package  
ADD http://downloads.haprotec.de/create-deb-package/create-deb-package.deb /  
RUN dpkg -i ./create-deb-package.deb && rm create-deb-package.deb  

