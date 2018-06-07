FROM debian:stretch  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -qy install --no-install-recommends \  
python \  
ca-certificates \  
gcc \  
libc6-dev \  
python-dev \  
atool \  
bzip2 \  
libffi6 \  
libffi-dev \  
libssl1.1 \  
libssl-dev \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install --no-cache-dir https://github.com/jsza/tempus-map-
updater/zipball/master \  
&& /usr/local/bin/twistd \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qy remove libffi-dev libssl-dev gcc
libc6-dev \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qy autoremove  
RUN adduser --uid 5000 \--disabled-password --gecos "" steam  
  
USER steam  
  
WORKDIR /home/steam  
ENTRYPOINT ["/usr/local/bin/twistd", "-n", "mapupdater"]  

