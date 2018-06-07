############################################################  
# Dockerfile to build Paintomics 3 container images  
# Based on httpd  
############################################################  
  
# Set the base image to official Httpd  
FROM httpd  
  
# File Author / Maintainer  
MAINTAINER Rafa Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
  
RUN apt-get update \  
&& apt-get install -y python-dev python-mysqldb python-rsvg python-cairo
python-cairosvg python-imaging python-pip libatlas-base-dev gfortran
libapache2-mod-wsgi r-base r-base-dev mongodb-clients wget \  
&& pip install flask gevent numpy enum configparser pymongo scriptine datetime
scipy psutil apscheduler  
  
RUN R --no-save -e "install.packages('amap',
repos='http://cran.us.r-project.org'); q();"  
  
RUN wget -O /tmp/paintomics.zip
https://github.com/fikipollo/paintomics3/archive/release/last.zip  
  
RUN unzip /tmp/paintomics.zip -d /tmp/paintomics \  
&& mv /tmp/paintomics/*/* /usr/local/apache2/htdocs/ \  
&& rm -r /tmp/paintomics/ \  
&& rm /tmp/paintomics.zip \  
&& sed -i 's/application\\.launch/#application\\.launch/'
/usr/local/apache2/htdocs/PaintomicsServer/src/launch_server.py  
  
COPY configs/example_serverconf.py
/usr/local/apache2/htdocs/PaintomicsServer/src/resources/example_serverconf.py  
COPY configs/entrypoint.sh /usr/bin/entrypoint.sh  
COPY configs/httpd.conf /usr/local/apache2/conf/httpd.conf  
COPY configs/paintomics.wsgi
/usr/local/apache2/htdocs/PaintomicsServer/paintomics.wsgi  
  
RUN chmod +x /usr/bin/entrypoint.sh \  
&& chown -R www-data:www-data /usr/local/apache2/htdocs/  
  
##################### INSTALLATION END #####################  
  
VOLUME ["/data/paintomics3"]  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

