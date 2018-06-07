FROM atlassian/default-image  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -qy --no-install-recommends \  
python3.4 \  
python3.4-dev \  
python3-pip \  
python3-lxml \  
cloc \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -xe \  
&& pip3 install "Django<1.9" libsass wheel boto  

