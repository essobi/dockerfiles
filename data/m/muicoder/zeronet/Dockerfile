FROM muicoder/glibc:alpine  
  
ARG BRANCH=master  
ARG WORK=/opt  
  
  
RUN apk --no-cache add libressl \  
py2-gevent \  
py2-msgpack \  
tor && \  
curl -sSL https://github.com/muicoder/zeronet/raw/master/torrc -o
/etc/tor/torrc  
  
RUN mkdir -p $WORK && \  
wget -qO- https://github.com/HelloZeroNet/ZeroNet/archive/$BRANCH.tar.gz | tar
-xzf - -C $WORK && \  
cd $WORK/ZeroNet-$BRANCH && \  
mkdir -p data log && \  
echo -e '#!/bin/sh\n\ncd "$(dirname "$(realpath "$0")")"\ntor &\npython -B
zeronet.py --ui_ip ${IP:-127.0.0.1} --ui_port ${PORT:-43110}' > launch && \  
chmod +x launch  
  
VOLUME ["$WORK/ZeroNet-$BRANCH/data"]  
  
EXPOSE 43110  
ENV PATH=$PATH:$WORK/ZeroNet-$BRANCH  
CMD ["launch"]  

