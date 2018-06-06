FROM ubuntu:16.04  
MAINTAINER Marian Neagul <marian@info.uvt.ro>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update --fix-missing && \  
apt-get -y install unzip software-properties-common subversion && \  
/usr/bin/add-apt-repository ppa:ubuntugis/ppa && \  
apt-get -y update && \  
#  
# Download required packages  
#  
apt-get -y install crudini libmozjs185-1.0 libfcgi libyaml-0-2 libxslt1.1
libpython2.7 \  
flex bison libfcgi-dev libxml2 libxml2-dev curl openssl autoconf \  
apache2 python-software-properties libmozjs185-dev python-dev build-essential
\  
libxslt1-dev libcgal-dev libyaml-dev libgdal20 libgdal1-dev build-essential \  
cmake ninja libmuparser2v5 libmuparser-dev \  
libopencv-core2.4v5 libopencv-contrib2.4v5 libopencv-features2d2.4v5 \  
libopencv-flann2.4v5 libopencv-gpu2.4v5 libopencv-imgproc2.4v5 \  
libopencv-legacy2.4v5 libopencv-ml2.4v5 libopencv-objdetect2.4v5 \  
libopencv-ocl2.4v5 libopencv-photo2.4v5 libopencv-stitching2.4v5 \  
libopencv-superres2.4v5 libopencv-ts2.4v5 libopencv-dev \  
fftw2 fftw-dev libopenthreads-dev libopenthreads20 libossim1 libossim-dev \  
libtinyxml-dev libtinyxml2.6.2v5 gcc-4.9 g++-4.9 python-owslib python-gdal
gdal-bin python-pip && \  
pip install rasterio==1.0a12 &&\  
#  
# Build the tools  
#  
mkdir -p /root/packages /root/build/OTB /root/build/ITK && \  
svn checkout http://svn.zoo-project.org/svn/tags/rel-1.6.0/ /root/zoo-project
&& \  
curl -o /root/packages/OTB-5.4.0.tgz \  
https://www.orfeo-toolbox.org/packages/archives/OTB/OTB-5.4.0.tgz && \  
curl -o /root/packages/InsightToolkit-4.11.0.tar.gz \  
https://netcologne.dl.sourceforge.net/project/itk/itk/4.11/InsightToolkit-4.11.0.tar.gz
&& \  
tar -xzvf /root/packages/OTB-5.4.0.tgz -C /root/packages/ && \  
tar -xzvf /root/packages/InsightToolkit-4.11.0.tar.gz -C /root/packages/ && \  
cd /root/build/ITK && \  
cmake /root/packages/InsightToolkit-4.11.0/ \  
-DCMAKE_POSITION_INDEPENDENT_CODE=ON \  
-DBUILD_SHARED_LIBS=ON && \  
make -j 16 && \  
make install && \  
cd /root/build/OTB && \  
cmake /root/packages/OTB-5.4.0/ \  
-DCMAKE_POSITION_INDEPENDENT_CODE=ON \  
-DBUILD_SHARED_LIBS=ON && \  
make -j 4 && \  
make install && \  
#  
# Build Zoo  
# it is patched to build agains ITK 4.11  
#  
cd /root/zoo-project/thirds/cgic206 && make && \  
sed -ibak 's|-litkv3p_lsqr-$ITKVERS| |g' /root/zoo-project/zoo-project/zoo-
kernel/configure.ac && \  
cd /root/zoo-project/zoo-project/zoo-kernel && autoconf && \  
./configure --with-js --with-python \  
\--with-otb=/usr/local/ --with-otb-version=5.4 \  
\--with-itk=/usr/local --with-itk-version=4.11 && \  
make && make install && \  
ldconfig && \  
cd /root/zoo-project/zoo-project/zoo-kernel && ln -s
/usr/local/lib/libzoo_service.so* /usr/lib/ && \  
cp main.cfg /usr/lib/cgi-bin && \  
cp zoo_loader.cgi /usr/lib/cgi-bin && \  
/usr/bin/crudini --set /usr/lib/cgi-bin/main.cfg env ITK_AUTOLOAD_PATH
"/usr/local/lib/otb/applications" && \  
cp ../zoo-services/hello-py/cgi-env/*.zcfg /usr/lib/cgi-bin && \  
cp ../zoo-services/hello-py/cgi-env/*.py /usr/lib/cgi-bin/ && \  
mkdir -p /root/build/OTB2CFG/zcfgs && \  
cd /root/build/OTB2CFG && \  
cmake /root/zoo-project/thirds/otb2zcfg/ && \  
make && \  
cd /root/build/OTB2CFG/zcfgs && \  
ITK_AUTOLOAD_PATH=/usr/local/lib/otb/applications ../otb2zcfg && \  
mkdir -p /usr/lib/cgi-bin/OTB && \  
cp *zcfg /usr/lib/cgi-bin/OTB && \  
sed -i.bak 's|serverAddress.*|serverAddress = http://127.0.0.1|g'
/usr/lib/cgi-bin/main.cfg && \  
echo "ServerName wps-worker" >> /etc/apache2/conf-enabled/server-name.conf &&
\  
a2enmod cgi && \  
apt-get -y purge \  
libfcgi-dev libxml2-dev libmozjs185-dev python-dev libxslt1-dev libcgal-dev
libyaml-dev \  
libgdal1-dev libmuparser-dev libopencv-dev fftw-dev libopenthreads-dev
libossim-dev libtinyxml-dev \  
gcc gcc-4.9 g++-4.9 libopenexr-dev libfl-dev autotools-dev dpkg-dev libbison-
dev \  
libgdal1-dev software-properties-common subversion ninja cmake && \  
apt -y autoremove && \  
# Clean  
rm -fr /root/build/ /root/packages/ /root/zoo-project/  
RUN \  
mkdir -p /var/data && chown www-data:www-data /var/data && \  
mkdir -p /var/www/temp && chown www-data:www-data /var/www/temp && \  
mkdir -p /var/www/cache && chown www-data:www-data /var/www/cache  
RUN mkdir /eodata /eo4see  
VOLUME ["/eodata", "/eo4see"]  
EXPOSE 80  
ENTRYPOINT /usr/local/bin/docker-zoo-entrypoint.sh  
COPY entrypoint.sh /usr/local/bin/docker-zoo-entrypoint.sh  

