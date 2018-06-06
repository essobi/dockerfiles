FROM prima/php:7.2.5-2  
  
ENV
IMAGEMAGICK_SHA256=c670eff3b4ad7ea33d756e90e3ba4d6a03da774cd280b7f8e905e2d2c95a2b3a
\  
WKHTMLTOPDF_SHA256=049b2cdec9a8254f0ef8ac273afaf54f7e25459a273e27189591edc7d7cf29db
\  
GHOSTSCRIPT_SHA256=8341407ed12434bb248ecee081528f68429664d85c9bfbce883459dcbdd852bb  
  
# Prima php.ini  
COPY files/prima.ini /usr/local/etc/php/conf.d/prima.ini  
  
# Temporary RCE mitigation (https://imagetragick.com/), upgrade imagemagick as
soon as the proper fix is released  
COPY files/policy.xml /etc/ImageMagick/policy.xml  
  
# Entrypoint  
COPY files/entrypoint.sh /entrypoint.sh  
  
RUN echo "deb-src http://deb.debian.org/debian stretch main" >>
/etc/apt/sources.list && \  
echo "deb-src http://security.debian.org stretch/updates main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y redis-tools build-essential checkinstall curl && \  
apt-get -y build-dep imagemagick && \  
curl -L -o /opt/ghostscript.tgz https://github.com/ArtifexSoftware/ghostpdl-
downloads/releases/download/gs922/ghostscript-9.22-linux-x86_64.tgz && \  
cd /opt && \  
echo "${GHOSTSCRIPT_SHA256} ghostscript.tgz" | sha256sum -c \- && \  
tar xzf ghostscript.tgz && \  
rm ghostscript.tgz && \  
cd /opt/ghostscript-9.22-linux-x86_64 && \  
mv gs-922-linux-x86_64 /usr/bin/gs && \  
chmod +x /usr/bin/gs && \  
curl -L -o /opt/imagemagick.tar.gz
https://www.imagemagick.org/download/ImageMagick-7.0.7-35.tar.gz && \  
cd /opt && \  
echo "${IMAGEMAGICK_SHA256} imagemagick.tar.gz" | sha256sum -c \- && \  
tar xzf imagemagick.tar.gz && \  
rm imagemagick.tar.gz && \  
cd /opt/ImageMagick-7.0.7-35 && \  
./configure && \  
make -j $(nproc) && \  
make install && \  
apt-get install -y pdftk && \  
apt-get install -y xz-utils libxext6 libfontconfig1 libxrender-dev && \  
curl -L -o /opt/wkhtmltox.tar.xz
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
cd /opt && \  
echo "${WKHTMLTOPDF_SHA256} wkhtmltox.tar.xz" | sha256sum -c \- && \  
tar xf /opt/wkhtmltox.tar.xz -C /opt/ && \  
cp /opt/wkhtmltox/bin/* /usr/local/bin && \  
chmod +x /usr/local/bin/wkhtml* && \  
apt-get install -y python python-pip unzip rsync && \  
pip install supervisor --pre && \  
pip install --upgrade awscli && \  
aws configure set s3.signature_version s3v4 && \  
apt-get install -y bzip2 libfontconfig1 && \  
pecl install imagick && \  
echo "extension=imagick.so" > /usr/local/etc/php/conf.d/docker-php-ext-
imagick.ini && \  
apt-get -y remove \--purge xz-utils bzip2 build-essential checkinstall python-
pip && \  
rm -r /var/lib/apt/lists/* && \  
rm -rf /opt/ghostscript* /opt/ImageMagick* /opt/wkhtmltox* && \  
mkdir -p /var/log/prima && \  
gs --version && \  
convert --version && \  
wkhtmltopdf --version && \  
php -i | grep -i imagemagick && \  
supervisord --version  
  
EXPOSE 9001  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]  

