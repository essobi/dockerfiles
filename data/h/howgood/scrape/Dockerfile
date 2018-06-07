FROM debian:jessie  
  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
curl \  
python \  
python-dev \  
python-pip \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
tor \  
privoxy \  
&& pip install --upgrade pip \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y \  
&& apt-get autoremove -y  
  
COPY privoxy.conf /etc/privoxy/config  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENV http_proxy http://127.0.0.1:8118  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD /bin/bash  

