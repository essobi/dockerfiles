FROM alpine  
MAINTAINER b3vis  
# upgrade & install packages  
RUN \  
apk upgrade --no-cache \  
&& \  
apk add --no-cache \  
lame \  
sox \  
flac \  
python2 \  
py-setuptools \  
# install build packages  
&& \  
apk add --no-cache --virtual=build-dependencies \  
git \  
g++ \  
gcc \  
make \  
&& \  
# install redactedbetter  
git clone https://github.com/Mechazawa/REDBetter-crawler /tmp/REDBetter-
crawler \  
&& \  
cd /tmp/REDBetter-crawler \  
&& \  
python setup.py install \  
&& \  
# compile mktorrent  
git clone https://github.com/Rudde/mktorrent /tmp/mktorrent \  
&& \  
cd /tmp/mktorrent \  
&& \  
make clean install \  
&& \  
# cleanup  
apk del --purge --no-cache build-dependencies \  
&& \  
rm -rf /tmp/*  
#  
CMD ["/usr/bin/redactedbetter"]

