# radiantbluetechnologies/rialto-geoserver  
FROM radiantbluetechnologies/rialtobase-geoserver  
MAINTAINER mpg@flaxen.com  
  
ENV RIALTO_BRANCH=dev  
  
VOLUME /rialtodata  
  
ENV RIALTO_INPUT_DIR=/rialtodata/inputs  
ENV RIALTO_OUTPUT_DIR=/rialtodata/outputs  
  
##################################################################  
#  
#  
# Here we build the geopackage libraries (including pdal and ossim).  
# Since this docker image is build FROM rialtobase-geoserver, we can't  
# also be FROM the regular geopackage image. Instead, we grab the build script  
# from the geopackage github repo and build it all here manually.  
# If we had RPMs for ossim and pdal and geopackage, this would not be an
issue.  
ENV OSSIM_DEV_HOME=/tmp/sources/ossim \  
OSSIM_BUILD_DIR=/tmp/builds/ossim \  
OSSIM_DEPENDENCIES=/usr \  
OSSIM_PREFS_FILE=/usr/share/ossim/ossim_preferences \  
OSSIM_INSTALL_PREFIX=/usr \  
OSSIM_DATA=/usr/share/ossim \  
RIALTO_BRANCH=dev  
  
RUN true \  
&& curl -L https://github.com/radiantbluetechnologies/rialto-
geopackage/archive/$RIALTO_BRANCH.zip -o /tmp/geopackage-tmp.zip \  
&& unzip -d /tmp/sources/ /tmp/geopackage-tmp.zip \  
&& mv /tmp/sources/rialto-geopackage-$RIALTO_BRANCH/ /tmp/sources/geopackage-
tmp/ \  
&& cp /tmp/sources/geopackage-tmp/docker/build.sh /tmp/build2.sh \  
&& /tmp/build2.sh \  
&& rm -fr /tmp/geopackage-tmp.zip /tmp/sources/geopackage-tmp/ /tmp/build2.sh  
  
#  
#  
##################################################################  
RUN true \  
&& mkdir -p $OSSIM_DATA/elevation/srtm/1arc \  
&& curl -L
http://dds.cr.usgs.gov/srtm/version2_1/SRTM1/Region_01/N48W113.hgt.zip -o
/tmp/N48W113.hgt.zip \  
&& curl -L
http://dds.cr.usgs.gov/srtm/version2_1/SRTM1/Region_01/N48W114.hgt.zip -o
/tmp/N48W114.hgt.zip \  
&& curl -L
http://dds.cr.usgs.gov/srtm/version2_1/SRTM1/Region_01/N48W115.hgt.zip -o
/tmp/N48W115.hgt.zip \  
&& unzip -d $OSSIM_DATA/elevation/srtm/1arc/ /tmp/N48W113.hgt.zip \  
&& unzip -d $OSSIM_DATA/elevation/srtm/1arc/ /tmp/N48W114.hgt.zip \  
&& unzip -d $OSSIM_DATA/elevation/srtm/1arc/ /tmp/N48W115.hgt.zip  
  
COPY wps/json2wpsscript.py /tmp/json2wpsscript.py  
  
COPY wps/ossim-viewshed.json /tmp/ossim-viewshed.json  
COPY wps/ossim-slope.json /tmp/ossim-slope.json  
COPY wps/ossim-hlz.json /tmp/ossim-hlz.json  
  
COPY wps/vs.lut $OSSIM_DATA/vs.lut  
  
# install our WPS scrips  
COPY build.sh /tmp/build.sh  
RUN /tmp/build.sh  

