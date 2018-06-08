FROM osmtw/mapnik3:v3.0.11  
MAINTAINER Rex Tsai <rex.cc.tsai@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TILESTACHE_VERSION=1.49.8-3 \  
_UWSGI_VERSION_=2.0.12-5ubuntu3  
  
RUN apt-get update \  
&& apt-get install -y tilestache=$TILESTACHE_VERSION \  
uwsgi=$_UWSGI_VERSION_ uwsgi-plugin-python=$_UWSGI_VERSION_  
  
# Clean up APT when done  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

