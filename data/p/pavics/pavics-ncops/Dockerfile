FROM ubuntu:16.04  
  
RUN apt-get -yqq update && \  
apt-get -yqq install python python-nose python-zmq ipython python-numpy \  
python-scipy python-netcdf4 python-matplotlib \  
python-mpltoolkits.basemap python-pip apache2 \  
libapache2-mod-wsgi python-setuptools python-lxml \  
python-geojson python-future python-shapely \  
git-core curl && \  
pip install threddsclient  
  
RUN cd /root && \  
git clone -b fix_async https://github.com/bstdenis/pywps.git && \  
cd /root/pywps && \  
python setup.py install && \  
mkdir /var/www/html/wps && \  
mkdir /var/www/html/wps_results && \  
useradd apapywps && \  
mkdir /home/apapywps && \  
chown apapywps /home/apapywps && \  
chgrp apapywps /home/apapywps && \  
chown apapywps /var/www/html/wps_results && \  
chgrp apapywps /var/www/html/wps_results && \  
rm -rf /root/pywps && \  
cd /root && \  
git clone -b slices1 https://github.com/Ouranosinc/pyPavics.git && \  
cd /root/pyPavics && \  
python setup.py install && \  
rm -rf /root/pyPavics && \  
chown apapywps /opt && \  
chgrp apapywps /opt && \  
chown apapywps /tmp && \  
chgrp apapywps /tmp && \  
mkdir /var/www/html/wps_results/pavics-ncops && \  
chown apapywps /var/www/html/wps_results/pavics-ncops && \  
chgrp apapywps /var/www/html/wps_results/pavics-ncops  
  
COPY pywps.wsgi /var/www/html/wps/  
COPY apache2.conf /etc/apache2/  
COPY pywps.cfg /etc/  
COPY wps_processes/wps_*.py /var/www/html/wps/  
COPY ncops.cfg /home/  
  
CMD export GEOSERVER_HOST=$(grep \--only-matching --perl-regex
"(?<=GEOSERVER_HOST\=).*" /home/ncops.cfg) && \  
export WPS_HOST=$(grep \--only-matching --perl-regex "(?<=WPS_HOST\=).*"
/home/ncops.cfg) && \  
printf "\nexport GEOSERVER_HOST=\"$GEOSERVER_HOST\"\n" >> /etc/apache2/envvars
&& \  
sed -i '/outputurl=/c\outputurl=http://'"$WPS_HOST"'/wps_results/pavics-
ncops/' /etc/pywps.cfg && \  
/etc/init.d/apache2 start && tail -f /dev/null  
  
EXPOSE 80  

