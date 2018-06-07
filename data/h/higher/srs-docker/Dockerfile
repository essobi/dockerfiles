FROM buildpack-deps:stretch  
  
RUN set -ex \  
&& buildDeps=' \  
unzip \  
sudo \  
# "install CherryPy-3.2.4" require sudoer failed. ret=127 :(  
' \  
&& sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \  
&& apt-get update && apt-get install -y $buildDeps ffmpeg \--no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& mkdir /srs && git clone \--depth=1 https://github.com/ossrs/srs /tmp/srs &&
cd /tmp/srs/trunk \  
&& ./configure \--x86-x64 \--with-stream-caster \--jobs=16 \  
&& make -j16 \  
&& apt-get purge -y \--auto-remove $buildDeps \  
&& mv /tmp/srs/trunk/objs /srs/objs \  
&& rm -rf /tmp/srs \  
  
WORKDIR /srs  
VOLUME /srs/objs/nginx/html  
  
ENTRYPOINT ["/srs/objs/srs"]  
CMD ["-c", "conf/rtmp.conf"]  

