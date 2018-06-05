FROM articulate/articulate-node:8  
ARG vips_version=8.6.2  
ENV LD_LIBRARY_PATH=/usr/local/lib  
ARG gifsicle_version=1.91  
RUN apt-get update && \  
apt-get install -y build-essential graphicsmagick-libmagick-dev-compat
libexpat1-dev libfftw3-dev liborc-0.4-dev libpng-dev libtiff5-dev pngquant &&
\  
apt-get clean  
  
WORKDIR /tmp  
  
RUN mkdir -p vips && \  
curl -Ls
https://github.com/jcupitt/libvips/releases/download/v${vips_version}/vips-${vips_version}.tar.gz
| tar xzC vips --strip-components=1 && \  
cd vips && \  
./configure --disable-static && \  
make && make install && make clean && \  
cd ..  
  
ADD https://github.com/kohler/gifsicle/archive/v${gifsicle_version}.zip
gifsicle.zip  
RUN unzip gifsicle.zip && \  
cd gifsicle-${gifsicle_version} && \  
autoreconf -i && \  
./configure --disable-gifview --disable-gifdiff && \  
make install  
  
RUN rm -rf /tmp/*  
WORKDIR $SERVICE_ROOT  

