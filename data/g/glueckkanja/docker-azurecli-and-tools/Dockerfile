FROM microsoft/azure-cli  
  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN echo "deb http://deb.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list \  
&& apt-get update \  
&& apt-get -qqy upgrade \  
&& apt-get install -yq \  
zip \  
sendemail \  
python-pip \  
python-dev \  
zlib1g-dev \  
libjpeg-dev \  
vncsnapshot \  
ffmpeg \  
jq \  
&& pip install vncdotool \  
&& pip install service_identity \  
&& npm install -g shelljs \  
&& apt-get install -yq cifs-utils screen rsync \  
&& curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash \  
&& apt-get install -yq git-lfs \  
&& git lfs install \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

