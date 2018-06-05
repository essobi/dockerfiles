FROM alpine:3.6  
# if you add shit to this, pay attention to the order.  
# we install a full fledged version of python and all the  
# tools for pip and then we get rid of them all after we  
# install our pip modules and install a minimal python version  
# This saves about 200MB of size... we get rid of all the apt files for good
measure.  
RUN apk add --update --no-cache \  
musl-utils \  
musl-dev \  
musl \  
&& \  
echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk add --update --no-cache \  
libevent@edge\  
libcouchbase@community \  
libcouchbase-libevent@community \  
libcouchbase-dev@community \  
libcouchbase-bin@community \  
libressl2.5-libcrypto@edge \  
libressl2.5-libssl@edge \  
python3 \  
build-base \  
python3-dev \  
bash \  
wget \  
ca-certificates \  
&& \  
apk add --no-cache --virtual=build-dependencies && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
pip3 install \  
amqplib \  
celery \  
couchbase \  
# docker-py==1.10.6 \ i THINK compose will install this for us  
httplib2 \  
redis \  
redis-py-cluster \  
pika \  
pymongo \  
PyMySQL \  
pympler \  
sh \  
&& \  
apk del build-dependencies build-base python3-dev && \  
rm -r /root/.cache && \  
rm -r /usr/lib/python*/__pycache__ && \  
rm -r /usr/lib/python*/tkinter/__pycache__ && \  
rm -r /usr/lib/python*/pydoc_data/__pycache__ && \  
rm -r /usr/lib/python*/idlelib/__pycache__ && \  
rm -r /usr/lib/python*/encodings/__pycache__ && \  
rm -r /usr/lib/python*/asyncio/__pycache__ && \  
rm -r /usr/share/terminfo  

