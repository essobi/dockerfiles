FROM postgres:10  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
gcc libc6-dev python3-dev libffi-dev libevent-dev lzop pv gnupg \  
libssl-dev curl runit && \  
rm -rf /var/lib/apt/lists/*  
COPY requirements.txt wal-e.conf recovery.conf \  
/usr/share/wal-e/  
RUN \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py && \  
python3 -m pip install \--requirement /usr/share/wal-e/requirements.txt  
COPY 00setup-conf.d.sh setup-wal-e.sh /docker-entrypoint-initdb.d/  

