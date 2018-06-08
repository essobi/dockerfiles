FROM fedora:24  
MAINTAINER "Florian Ludwig" <f.ludwig@greyrook.com>  
  
RUN dnf -y update \  
&& dnf -y install python-pip \  
python-devel \  
&& dnf clean all \  
&& pip install --no-cache-dir --upgrade pip  
  
COPY ./install_fedora_deps.py /usr/local/bin/install_fedora_deps.py  
  
  
# RUN mkdir -p /app && touch /app/pre-install.sh && touch /app/after-
install.sh && chmod +x /app/*.sh  
  
# WORKDIR /app  
# ONBUILD COPY . /app/  
# ONBUILD RUN /app/pre-install.sh && \  
# install_fedora_deps.py /app/requirements.txt && \  
# pip install -e /app && \  
# pip install --no-cache-dir -r /app/requirements.txt && \  
# /app/pre-install.sh  

