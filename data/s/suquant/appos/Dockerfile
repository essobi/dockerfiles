ARG alpine_version=3.7  
FROM alpine:${alpine_version}  
LABEL maintainer="George Kutsurua <g.kutsurua@gmail.com>"  
  
ARG python_version=3  
RUN apk add \--no-cache sudo bash curl rsync openssl openssh-client nginx \  
libpq libffi libxml2 libbz2 \  
libxslt libtool libstdc++ zlib git unzip \  
libjpeg libjpeg-turbo openjpeg \  
libpng tiff freetype lcms2 \  
libwebp tcl imagemagick imagemagick-c++ \  
json-c jsoncpp python${python_version} musl \  
coreutils ca-certificates \  
pcre libpcre32 postgresql ffmpeg &&\  
wget -O - https://bootstrap.pypa.io/get-pip.py | python${python_version} &&\  
ln -s /usr/bin/python${python_version} /usr/bin/python || true  
  
RUN apk add \--no-cache libffi-dev libxml2-dev libxslt-dev zlib-dev libjpeg-
turbo-dev \  
libpng-dev tiff-dev libwebp-dev tcl-dev openjpeg-dev freetype-dev \  
lcms2-dev imagemagick-dev json-c-dev jsoncpp-dev musl-dev \  
pcre-dev autoconf automake make perl swig postgresql-dev \  
gcc g++ linux-headers python${python_version}-dev  
ENV LANG=en_US.utf8 \  
LC_ALL=en_US.utf8 \  
LANGUAGE=en_US.utf8  
  
# Fix linking  
RUN mkdir /lib64 && ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
&& \  
for n in $(find /usr/lib -name 'libpython3*m*' -type f); do (ln -s $n `printf
"$n" | sed -E 's/python([0-9\\.]+)m(.+)/python\1\2/'`); done  
  
ARG geos_version=3.6.2  
RUN mkdir /tmp/build-geos && \  
cd /tmp/build-geos && \  
wget http://download.osgeo.org/geos/geos-${geos_version}.tar.bz2 && \  
cd /tmp/build-geos && \  
tar xjf geos-${geos_version}.tar.bz2 && \  
cd geos-${geos_version} && \  
./configure \--prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--localstatedir=/var \  
\--enable-python && \  
make && make check && make install && \  
rm -rf /tmp/build-geos  
  
ARG proj_version=4.9.3  
ARG proj_datumgrid_version=1.6  
RUN mkdir /tmp/build-proj && \  
cd /tmp/build-proj && \  
wget http://download.osgeo.org/proj/proj-${proj_version}.tar.gz && \  
wget http://download.osgeo.org/proj/proj-
datumgrid-${proj_datumgrid_version}.zip && \  
tar xzf proj-${proj_version}.tar.gz && \  
cd proj-${proj_version}/nad && \  
unzip ../../proj-datumgrid-${proj_datumgrid_version}.zip && \  
cd .. && \  
./configure \--prefix=/usr &&\  
make && make install && \  
rm -rf /tmp/build-proj  
  
ARG gdal_version=2.2.3  
RUN mkdir /tmp/build-gdal && \  
cd /tmp/build-gdal && \  
wget
http://download.osgeo.org/gdal/${gdal_version}/gdal-${gdal_version}.tar.gz &&
\  
tar xzf gdal-${gdal_version}.tar.gz && \  
cd gdal-${gdal_version} && \  
./configure \--prefix=/usr \  
\--with-python=yes \  
\--with-geos=yes && \  
make && make install && \  
rm -rf /tmp/build-gdal  
  
ONBUILD COPY ssh-key requirements.txt /app/  
  
ONBUILD RUN chmod 600 /app/ssh-key && \  
eval $(ssh-agent) && \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
ssh-add /app/ssh-key && \  
pip install -r /app/requirements.txt  
  
ONBUILD RUN rm -rf /app/*  
  
# Delete dev pkgs  
ONBUILD RUN apk del \--force libffi-dev libxml2-dev libxslt-dev zlib-dev
libjpeg-turbo-dev \  
libpng-dev tiff-dev libwebp-dev tcl-dev openjpeg-dev freetype-dev \  
lcms2-dev imagemagick-dev json-c-dev jsoncpp-dev musl-dev \  
pcre-dev autoconf automake make perl swig postgresql-dev \  
gcc g++ linux-headers python${python_version}-dev  

