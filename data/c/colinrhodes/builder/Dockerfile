#  
# Builder Dockerfile  
# An image for building uwsgi packages for production  
#  
FROM colinrhodes/pypy  
  
MAINTAINER Colin Rhodes <colin@colin-rhodes.com>  
  
ADD libpypy-c.so /usr/lib/libpypy-c.so  
  
RUN apt-get -yq update  
RUN apt-get -yq --no-install-recommends install build-essential libssl-dev
pypy-dev libjansson-dev libjansson4 python-dev libpcre3-dev librados-dev  
  
ADD uwsgi-2.0.4.tar.gz /src/  
ADD redis-2.8.9.tar.gz /src/  
  
ENV PREFIX /opt/redis  
  
RUN cd /src/redis-2.8.9 && make && make install  
  
WORKDIR /src/uwsgi-2.0.4  
  
RUN mkdir -p /opt/uwsgi/ && \  
make && python uwsgiconfig.py --build core && \  
python uwsgiconfig.py --plugin plugins/python core && \  
python uwsgiconfig.py --plugin plugins/pypy core && \  
python uwsgiconfig.py --plugin plugins/rados core && \  
mv uwsgi *.so /opt/uwsgi/  
  
WORKDIR /opt  
  
RUN tar -cf redis-2.8.9-bin.tar redis && \  
tar -cf uwsgi-2.0.4-core-bin.tar uwsgi && \  
gzip redis-2.8.9-bin.tar && gzip uwsgi-2.0.4-core-bin.tar  
  
CMD ["/bin/bash"]  

