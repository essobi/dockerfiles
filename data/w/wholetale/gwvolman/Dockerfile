FROM ubuntu:xenial  
  
RUN apt-get update -qqy && \  
apt-get install -qy software-properties-common python-software-properties && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy install \  
build-essential \  
vim \  
git \  
wget \  
python \  
fuse \  
davfs2 \  
libffi-dev \  
libssl-dev \  
libjpeg-dev \  
zlib1g-dev \  
libfuse-dev \  
libpython-dev && \  
apt-get -qqy clean all && \  
echo "user_allow_other" >> /etc/fuse.conf && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
  
COPY requirements.txt /gwvolman/requirements.txt  
COPY setup.py /gwvolman/setup.py  
COPY gwvolman /gwvolman/gwvolman  
  
WORKDIR /gwvolman  
RUN pip install --no-cache-dir -r requirements.txt -e . && rm -rf /tmp/*  
  
COPY mount.c /tmp/mount.c  
RUN gcc -Wall -fPIC -shared -o /usr/local/lib/container_mount.so /tmp/mount.c
-ldl -D_FILE_OFFSET_BITS=64 && \  
rm /tmp/mount.c && \  
chmod +x /usr/local/lib/container_mount.so && \  
echo "/usr/local/lib/container_mount.so" > /etc/ld.so.preload  
  
RUN useradd -g 100 -G 100 -u 1000 -s /bin/bash wtuser  
  
RUN girder-worker-config set celery backend redis://redis/ && \  
girder-worker-config set celery broker redis://redis/ && \  
girder-worker-config set girder_worker tmp_root /tmp  
  
ENV C_FORCE_ROOT=1  
ENTRYPOINT ["python", "-m", "girder_worker", "-l", "INFO"]  

