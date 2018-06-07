FROM kelvinchen/base:latest  
  
RUN echo "deb http://deb.debian.org/debian stretch non-free" >
/etc/apt/sources.list.d/non-free.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
mediainfo unrar unzip \  
&& rm -rf /var/lib/apt/lists/*  

