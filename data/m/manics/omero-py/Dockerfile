FROM library/alpine:3.7  
MAINTAINER spli@dundee.ac.uk  
  
# Basic utilities and Ice runtime libraries  
RUN apk \--no-cache add \  
curl \  
db \  
bzip2 \  
expat \  
libstdc++ \  
openssl \  
python2 \  
py2-pip  
  
# Can't use "pip install zeroc-ice==3.6.4" because musl is missing the  
# non-standard glibc symbols PTHREAD_MUTEX_*_NP  
# http://elias.rhi.hi.is/libc/Mutexes.html  
# This has been fixed in 3.7.1  
# https://github.com/zeroc-
ice/ice/commit/bf1057ad57b46bda03ebc5c7ce58358d94e448fc  
# Ice build  
RUN apk \--no-cache add \--virtual build-dependencies \  
gcc \  
g++ \  
db-dev \  
bzip2-dev \  
expat-dev \  
openssl-dev \  
python2-dev && \  
cd /root && \  
curl -sfL
https://files.pythonhosted.org/packages/c4/a8/1ffbaecab4b3a9892529c16a8c6323e37e5467447aa7a92955d68f6c5c45/zeroc-
ice-3.6.4.tar.gz | tar -zxf - && \  
cd zeroc-ice-3.6.4 && \  
sed -i.bak s/PTHREAD_MUTEX_ERRORCHECK_NP/PTHREAD_MUTEX_ERRORCHECK/
./src/ice/cpp/include/IceUtil/Mutex.h && \  
sed -i.bak s/PTHREAD_MUTEX_RECURSIVE_NP/PTHREAD_MUTEX_RECURSIVE/
./src/ice/cpp/src/IceUtil/RecMutex.cpp && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rf zeroc-ice-3.6.4 && \  
apk del build-dependencies  
  
# Get rid of the annoying "ERROR:omero.gateway:No Pillow installed" message  
ADD no-pillow-message.patch /root/  
RUN apk \--no-cache add \  
# omego requires six \  
py2-six && \  
mkdir -p /opt/omero && \  
pip install omego && \  
cd /opt/omero && \  
omego download py \--sym OMERO.py && \  
rm OMERO.py*zip && \  
ln -s /opt/omero/OMERO.py/bin/omero /usr/local/bin/ && \  
adduser -h /opt/omero -D omero && \  
chown -R omero:omero /opt/omero/OMERO.py/ && \  
patch -p0 < /root/no-pillow-message.patch  
# OMERO.web requirements \  
#RUN apk --no-cache add \  
# py-pillow  
# py-jinja2 \  
# py-gunicorn \  
# py-redis \  
# py-yaml && \  
# pip install -r /opt/omero/OMERO.py/share/web/requirements-py27.txt  
  
USER omero  
CMD ["omero"]  

