# Mapnik for Docker  
FROM ubuntu:14.04  
MAINTAINER Aldo Ridhoni<aldoridhoni@gmail.com>  
# Mapnik for Docker  
FROM ubuntu:latest  
ENV LANG C.UTF-8  
ENV LD_LIBRARY_PATH /lib:/usr/lib:/usr/local/lib  
RUN update-locale LANG=C.UTF-8  
  
# Essential stuffs  
RUN apt-get update && apt-get -qq install -y --no-install-recommends \  
build-essential \  
sudo \  
software-properties-common \  
curl \  
unzip  
  
# Boost  
RUN apt-get -qq install -y --no-install-recommends \  
libboost-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libboost-python-dev \  
libboost-regex-dev \  
libboost-system-dev \  
libboost-thread-dev  
  
# Mapnik dependencies  
RUN apt-get -qq install -y --no-install-recommends \  
libicu-dev \  
libtiff5-dev \  
libfreetype6-dev \  
libpng12-dev \  
libxml2-dev \  
libproj-dev \  
libsqlite3-dev \  
libgdal-dev \  
libcairo-dev \  
python-cairo-dev \  
postgresql-contrib \  
libharfbuzz-dev  
  
# Mapnik 3.0.10  
RUN curl -s
https://mapnik.s3.amazonaws.com/dist/v3.0.10/mapnik-v3.0.10.tar.bz2 | tar -xj
-C /tmp/ \  
&& cd /tmp/mapnik-v3.0.10 \  
&& python scons/scons.py configure JOBS=4 \  
&& make && make install JOBS=4 \  
&& cd / && rm -rf /tmp/mapnik-v3.0.10  
  
# pip  
RUN cd /tmp/ && curl --insecure -Os https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& rm get-pip.py  
  
# Python Mapnik  
RUN cd /tmp && curl -L https://github.com/mapnik/python-
mapnik/archive/master.zip -o python-mapnik.zip \  
&& unzip python-mapnik.zip \  
&& rm python-mapnik.zip \  
&& cd python-mapnik-master \  
&& python setup.py install \  
&& rm -rf ../python-mapnik-master  
  
# TileStache and dependencies  
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib  
RUN pip install -U Pillow modestmaps simplejson werkzeug mapbox-vector-tile
shapely numpy  
RUN mkdir -p /etc/tilestache  
COPY etc/run_tilestache.py /etc/tilestache/  
RUN cd /tmp && curl -L
https://github.com/aldoridhoni/TileStache/archive/integration-1.zip -o
tilestache.zip \  
&& unzip -q tilestache.zip \  
&& rm tilestache.zip \  
&& cd TileStache-integration-1 \  
&& python setup.py install \  
&& rm -rf ../Tilestache-integration-1  
  
# Uwsgi  
RUN pip install uwsgi && mkdir -p /etc/uwsgi/apps-enabled && mkdir -p
/etc/uwsgi/apps-available  
COPY etc/uwsgi_tilestache.ini /etc/uwsgi/apps-available/tilestache.ini  
RUN ln -s /etc/uwsgi/apps-available/tilestache.ini /etc/uwsgi/apps-
enabled/tilestache.ini  
  
# Supervisor  
RUN pip install supervisor  
RUN echo_supervisord_conf > /etc/supervisord.conf && printf
"[include]\\\nfiles = /etc/supervisord/*" >> /etc/supervisord.conf  
RUN mkdir -p /etc/supervisord  
COPY etc/supervisor_uwsgi.ini /etc/supervisord/uwsgi.ini  
COPY etc/supervisor_inet.conf /etc/supervisord/inet.conf  
COPY etc/supervisor_nginx.ini /etc/supervisord/nginx.conf  
  
# Nginx  
RUN add-apt-repository -y ppa:nginx/stable \  
&& apt-get -qq update \  
&& apt-get -qq install -y nginx \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y  
COPY etc/nginx_site.conf /etc/nginx/sites-available/site.conf  
RUN ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/  
RUN rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 80 9001  
ENV HOST_IP `ifconfig | grep inet | grep Mask:255.255.255.0 | cut -d ' ' -f 12
| cut -d ':' -f 2`  
  
CMD ["supervisord", "-n"]  
  

