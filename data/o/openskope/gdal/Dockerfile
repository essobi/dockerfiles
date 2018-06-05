from openskope/base:0.1.1  
ARG DEBIAN_FRONTEND=noninteractive  
USER root  
  
ENV DOCKER_IMAGE_NAME openskope/gdal  
  
RUN echo '***** Install Python2, Python3, and pip for both *****' \  
&& apt-get -y install python python-pip python3 python3-pip \  
&& pip2 install --upgrade pip \  
&& pip3 install --upgrade pip \  
\  
&& echo '***** install numpy package for both Python2 and Python3 *****' \  
&& pip2 install numpy \  
&& pip3 install numpy \  
\  
&& echo '***** download source package for GDAL 2.1.2 *****' \  
&& mkdir -p /tmp/builds \  
&& cd /tmp/builds \  
&& wget http://download.osgeo.org/gdal/2.1.2/gdal-2.1.2.tar.gz \  
&& gunzip gdal-2.1.2.tar.gz \  
&& tar -xvvf gdal-2.1.2.tar \  
\  
&& echo '***** configure and build GDAL with Python2 bindings ******' \  
&& cd /tmp/builds/gdal-2.1.2 \  
&& mkdir -p /opt/gdal \  
&& ./configure --prefix /opt/gdal/gdal-2.1.2 --with-python=$(which python2) \  
&& make install \  
\  
&& echo '***** then reconfigure and rebuild for Python3 bindings *****' \  
&& ./configure --prefix /opt/gdal/gdal-2.1.2 --with-python=$(which python3) \  
&& make install \  
\  
&& echo '**** clean up GDAL build directories *****' \  
&& rm -rf /tmp/builds  
  
ENV LD_LIBRARY_PATH=/opt/gdal/gdal-2.1.2/lib/  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/gdal/gdal-2.1.2/bin/  
ENV PYTHONPATH=/opt/gdal/gdal-2.1.2/lib/python2.7/site-packages/  
  
USER skope  
  
ENV SELFTEST_DIR ${SELFTEST_BASE}/${DOCKER_IMAGE_NAME}  
COPY ./selftest/expected.txt ${SELFTEST_BASE}  
COPY ./selftest/test.sh ${SELFTEST_DIR}/  
RUN ${SELFTEST_BASE}/runtest.sh  
  
CMD echo "Usage: docker run openskope/gdal <gdal-command> [gdal-command-
arguments]"  

