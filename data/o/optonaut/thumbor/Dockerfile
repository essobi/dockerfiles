FROM python:2  
MAINTAINER Johannes Schickling <schickling@optonaut.co>  
  
VOLUME /logs  
VOLUME /data  
  
# Things required for a python/pip environment  
COPY system-requirements.txt /usr/src/app/system-requirements.txt  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y autoremove && \  
xargs apt-get -y -q install < /usr/src/app/system-requirements.txt && \  
apt-get clean  
  
ENV HOME /usr/src/app  
ENV SHELL bash  
ENV WORKON_HOME /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/requirements.txt  
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt  
  
# install open cv  
RUN \  
wget https://github.com/Itseez/opencv/archive/3.0.0.tar.gz && \  
tar xvzf 3.0.0.tar.gz && \  
rm 3.0.0.tar.gz && \  
cd opencv-3.0.0 && \  
apt-get install -y cmake && \  
cmake . && \  
make && \  
make install && \  
cp lib/cv2.so /usr/local/lib/python2.7/ && \  
cd .. && \  
rm -rf opencv-3.0.0 && \  
apt-get remove -y cmake && \  
apt-get clean  
  
COPY conf/thumbor.conf.tpl /usr/src/app/thumbor.conf.tpl  
  
# build native custom_filters  
COPY custom_filters /usr/src/app/custom_filters  
RUN \  
cd custom_filters && \  
python setup.py build && \  
cp build/lib.linux-x86_64-2.7/custom_filters/*.so . && \  
rm -rf build  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["thumbor"]  
  
EXPOSE 80  

