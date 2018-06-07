FROM centos:7  
LABEL maintainer "Mikko Rauhala <mikko@meteo.fi>"  
  
ENV SMARTMET_DEVEL=0 \  
SMARTMET_LIBRARIES="newbase macgyver gis giza spine locus tron imagine" \  
SMARTMET_ENGINES="sputnik querydata geonames observation gis contour" \  
SMARTMET_PLUGINS="autocomplete timeseries download admin backend meta wfs
frontend wms" \  
MAKEFLAGS="-j8"  
RUN mkdir -p /usr/local/src/smartmet /smartmet/data /etc/smartmet/plugins
/etc/smartmet/engines /var/log/smartmet /var/smartmet/timeseriescache  
  
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rpm -ivh
https://download.postgresql.org/pub/repos/yum/9.3/redhat/rhel-7-x86_64/pgdg-
centos93-9.3-3.noarch.rpm && \  
yum -y update && yum -y install \  
bzip2-devel \  
cairo-devel cairo-gobject-devel \  
elfutils-devel \  
file \  
fmt-devel \  
gcc gcc-c++ \  
gdal-devel \  
geos-devel \  
gdk-pixbuf2-devel \  
git \  
grib_api grib_api-devel \  
gobject-introspection-devel \  
jemalloc-devel \  
jsoncpp-devel \  
libaio-devel \  
libcroco-devel \  
libtool \  
libatomic \  
libconfig-devel \  
libicu-devel \  
libjpeg-devel \  
libpqxx-devel \  
libspatialite-devel \  
make cmake imake \  
mariadb-devel \  
mysql++-devel \  
netcdf-devel netcdf-cxx-devel \  
openssl-devel \  
pango-devel \  
protobuf-devel protobuf-compiler \  
postgresql93-devel \  
python-devel\  
soci-devel soci-sqlite3-devel \  
sqlite-devel \  
unzip \  
wget \  
xqilla-devel \  
xerces-c-devel \  
zlib-devel && \  
rpm -ivh
http://download.weatherproof.fi/fmiforge/rhel/7/x86_64/librsvg2-2.40.6-3.el7.x86_64.rpm
\  
http://download.weatherproof.fi/fmiforge/rhel/7/x86_64/librsvg2-devel-2.40.6-3.el7.x86_64.rpm
&& \  
# ctpp2  
cd /usr/local/src/smartmet && \  
wget -nv http://ctpp.havoc.ru/download/ctpp2-2.8.3.tar.gz && \  
tar zxvf ctpp2-2.8.3.tar.gz && \  
cd ctpp2-2.8.3 && \  
cmake . && \  
sed -i '/#include <stdlib.h>/a #include <unistd.h>'
src/CTPP2FileSourceLoader.cpp && \  
make && \  
make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf /usr/local/src/smartmet/ctpp2-2.8.3;
fi && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf
/usr/local/src/smartmet/ctpp2-2.8.3.tar.gz; fi && \  
# boost  
cd /usr/local/src/smartmet && \  
wget -nv
http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz
&& \  
tar zxf boost_1_55_0.tar.gz && \  
cd boost_1_55_0 && \  
./bootstrap.sh \--without-libraries=mpi,graph_parallel && \  
./b2 $MAKEFLAGS && \  
./b2 install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf
/usr/local/src/smartmet/boost_1_55_0; fi && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf
/usr/local/src/smartmet/boost_1_55_0.tar.gz; fi && \  
# librsvg  
# cd /usr/local/src/smartmet && \  
# wget
http://ftp.gnome.org/pub/gnome/sources/librsvg/2.40/librsvg-2.40.6.tar.xz && \  
# tar xvf librsvg-2.40.6.tar.xz && \  
# cd librsvg-2.40.6 && \  
# export CPPFLAGS="-I/usr/include/glib-2.0/" && \  
# ./configure --disable-static --disable-gtk-doc --disable-gtk-theme --enable-
introspection && \  
# make && make install && \  
# if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf
/usr/local/src/smartmet/librsvg-2.40.6; fi && \  
# if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf
/usr/local/src/smartmet/librsvg-2.40.6.tar.xz; fi && \  
# ldconfig  
echo "/usr/local/lib/" > /etc/ld.so.conf.d/local.conf && ldconfig -v && \  
#  
# SmartMet Timezones  
#  
cd /usr/local/src/smartmet && \  
git clone https://github.com/fmidev/smartmet-timezones.git && \  
cd smartmet-timezones && \  
make && make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then rm -rf /usr/local/src/smartmet/smartmet-
timezones; fi && \  
#  
# SmartMet Libraries  
#  
for LIBRARY in ${SMARTMET_LIBRARIES}; \  
do \  
cd /usr/local/src/smartmet && \  
git clone https://github.com/fmidev/smartmet-library-${LIBRARY}.git && \  
cd smartmet-library-${LIBRARY} && \  
make && make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then strip /usr/lib64/libsmartmet-${LIBRARY}.so;
rm -rf /usr/local/src/smartmet/smartmet-library-${LIBRARY}; fi \  
done && \  
#  
# SmartMet server  
#  
cd /usr/local/src/smartmet && \  
git clone https://github.com/fmidev/smartmet-server.git && \  
cd smartmet-server && \  
make && make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then strip /usr/sbin/smartmetd; rm -rf
/usr/local/src/smartmet/smartmet-server; fi && \  
#  
# SmartMet Server Engines  
#  
for ENGINE in ${SMARTMET_ENGINES}; \  
do \  
cd /usr/local/src/smartmet && \  
git clone https://github.com/fmidev/smartmet-engine-${ENGINE}.git && \  
cd smartmet-engine-${ENGINE} && \  
make && make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then strip
/usr/share/smartmet/engines/${ENGINE}.so; rm -rf
/usr/local/src/smartmet/smartmet-engine-${ENGINE}; fi \  
done && \  
#  
# SmartMet Server Plugins  
#  
for PLUGIN in ${SMARTMET_PLUGINS}; \  
do \  
cd /usr/local/src/smartmet && \  
git clone https://github.com/fmidev/smartmet-plugin-${PLUGIN}.git && \  
cd smartmet-plugin-${PLUGIN} && \  
# CFLAGS="-DWITHOUT_AUTHENTICATION -DWITHOUT_OBSERVATION" make && make install
&& \  
CFLAGS="-DWITHOUT_AUTHENTICATION" make && make install && \  
if [ $SMARTMET_DEVEL -ne 1 ]; then strip
/usr/share/smartmet/plugins/${PLUGIN}.so; rm -rf
/usr/local/src/smartmet/smartmet-plugin-${PLUGIN}; fi \  
done && \  
#  
# Cleanup  
#  
yum -y --setopt=tsflags=noscripts remove libffi-devel && \  
yum -y erase '*-devel' && \  
yum -y erase 'perl-*' && \  
yum -y erase m4 make cpp cmake postgresql93 glibc-headers && \  
yum clean all && \  
rm -rf /usr/include /usr/local/include /usr/local/src /usr/share/doc \  
/usr/sbin/{glibc_post_upgrade.x86_64,sln} /usr/share/gnupg/help*.txt  
  
COPY smartmetconf /etc/smartmet  
RUN mkdir -p /smartmet/share  
COPY wms /smartmet/share/  
COPY dali /smartmet/share/  
  
HEALTHCHECK --interval=5m --timeout=3s \  
CMD curl -f http://localhost/admin?what=qengine || exit 1  
  
# Expose GeoServer's default port  
EXPOSE 80  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["smartmetd"]  

