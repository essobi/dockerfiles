FROM alpine  
  
RUN apk update; \  
apk add \  
python3 \  
python3-dev \  
squashfs-tools \  
tree \  
wget \  
openssl \  
ca-certificates \  
git \  
bash \  
util-linux \  
e2fsprogs \  
e2fsprogs-extra \  
ncurses  
  
RUN wget
'https://github.com/opencontainers/runc/releases/download/v1.0.0-rc4/runc.amd64'
-O /usr/local/bin/runc && \  
chmod 755 /usr/local/bin/runc  
  
RUN wget 'https://github.com/ihucos/runp/blob/master/runp?raw=true' -O
/usr/local/bin/runp && \  
chmod 4755 /usr/local/bin/runp  
  
RUN git clone https://github.com/ihucos/plash.git /opt/plash  
  
RUN echo '#!/bin/sh' > /usr/local/bin/plash  
RUN echo 'export PATH=/opt/plash/bin:$PATH' >> /usr/local/bin/plash  
RUN echo 'export PYTHONPATH=/opt/plash:PYTHONPATH' >> /usr/local/bin/plash  
RUN echo 'exec plash "$@"' >> /usr/local/bin/plash  
RUN chmod 755 /usr/local/bin/plash  

