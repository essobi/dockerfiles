FROM debian:jessie  
  
MAINTAINER Alphazo <alphazo@gmail.com>  
# Original Dockerfile from Silvio Fricke <silvio.fricke@gmail.com>  
# Updated to v1.0.6  
VOLUME /sourcedir /backupdir  
WORKDIR /borg  
  
ENTRYPOINT ["/usr/bin/borgctrl.sh"]  
CMD ["--help"]  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -y \  
&& apt-get install -y \  
build-essential \  
fakeroot \  
fuse \  
git-core \  
libacl1 \  
libacl1-dev \  
libssl-dev \  
openssl \  
python-virtualenv \  
python3-dev \  
liblz4-dev \  
python-lz4 \  
&& apt-get clean -y  
  
RUN git clone git://github.com/wallyhall/shini.git \  
&& cp shini/shini.sh /usr/bin/shini \  
&& chmod a+x /usr/bin/shini  
  
RUN virtualenv --python=python3 borg-env ; \  
. borg-env/bin/activate ; \  
pip install --upgrade pip ; \  
pip install cython ; \  
pip install tox  
  
ADD adds/borgctrl.sh /usr/bin/borgctrl.sh  
RUN chmod a+x /usr/bin/borgctrl.sh  
  
# the "git clone" is cached, we need to invalidate the docker cache here  
ADD
http://www.random.org/strings/?num=1&len=10&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new
uuid  
RUN git clone https://github.com/borgbackup/borg.git borg-git -b master; \  
. borg-env/bin/activate ; \  
pip install -e borg-git  

