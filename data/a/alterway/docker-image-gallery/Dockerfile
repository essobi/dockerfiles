FROM nginx:1  
ENV FGALLERY_VERSION 1.8.2  
RUN export DEBIAN_FRONTEND noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends curl imagemagick exiftran zip
liblcms2-utils libimage-exiftool-perl libjson-perl libjson-xs-perl jpegoptim
pngcrush p7zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# extract in /src, mv to /app  
RUN mkdir /fgallery \  
&& curl -sL
"https://github.com/wavexx/fgallery/archive/fgallery-${FGALLERY_VERSION}.tar.gz"
| tar xz -C /fgallery \  
&& ln -nsf "/fgallery/fgallery-fgallery-${FGALLERY_VERSION}/"* /fgallery  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
COPY noimages.html /  
  
VOLUME /images  
WORKDIR /images  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

