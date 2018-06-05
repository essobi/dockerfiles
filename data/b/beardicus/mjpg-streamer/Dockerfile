FROM debian:jessie  
MAINTAINER Brian Boucheron <brian@boucheron.org>  
  
RUN set -ex \  
&& buildDeps=' \  
git \  
gcc \  
g++ \  
make \  
cmake \  
ca-certificates \  
linux-headers-3.16.0-4-amd64 \  
libjpeg62-turbo-dev \  
' \  
&& runDeps=' \  
libjpeg62-turbo \  
' \  
&& apt-get update \  
&& apt-get install -y $buildDeps $runDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/jacksonliam/mjpg-streamer.git \  
&& cd /mjpg-streamer/mjpg-streamer-experimental \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /mjpg-streamer \  
&& apt-get purge -y --auto-remove $buildDeps  
  
EXPOSE 8080  
ENTRYPOINT ["mjpg_streamer"]  
  
CMD ["-i", "input_uvc.so", "-o", "'output_http.so -w /usr/local/share/mjpg-
streamer/www/'"]  

