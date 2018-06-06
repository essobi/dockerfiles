FROM daiko/mapserver  
MAINTAINER Florestan Bredow <florestan.bredow@daiko.fr>  
MAINTAINER Amandine Sahl <amandine.sahl@gmail.com>  
  
RUN apt-get update && apt-get -y install \  
libgdal-dev \  
build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY libs/erdas /usr/local/erdas  
RUN ln -s "/usr/local/erdas/lib/x64/release/libNCSEcw.so"
"/usr/local/lib/libNCSEcw.so" \  
&& ldconfig  
  
COPY libs/gdal-ecw/libgdal-ecw-1.10.0.tar.gz /usr/src/  
COPY libs/gdal-ecw/gdal-ecw-build /usr/bin/  
RUN gdal-ecw-build "/usr/local/erdas"  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

