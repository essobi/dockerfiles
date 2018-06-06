FROM debian:jessie  
LABEL maintainer="Nazar Mokrynskyi <nazar@mokrynskyi.com>"  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
# python-fontforge is needed by glyphIgo in runtime  
apt-get install -y \--no-install-recommends git ca-certificates g++ make
php5-cli python-fontforge && \  
git clone --recursive https://github.com/google/woff2.git && \  
cd woff2 && \  
make clean all && \  
mv woff2_compress woff2_decompress /usr/bin/ && \  
cd .. && \  
rm -rf woff2 && \  
git clone https://github.com/pettarin/glyphIgo.git && \  
mv glyphIgo/src/glyphIgo.py /usr/bin/glyphIgo && \  
rm -rf glyphIgo && \  
apt-get purge --auto-remove -y git ca-certificates g++ make && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY subset.php /  
  
CMD php subset.php  

