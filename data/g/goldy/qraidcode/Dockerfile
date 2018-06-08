FROM maxexcloo/nginx-php  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
ENV DEBIAN_FRONTEND noninteractive  
ADD apt-no-recommends /etc/apt/apt.conf.d/10-no-recommends  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y qrencode
git qrencode poppler-utils pngcrush php7.0-mcrypt php7.0-imagick php7.0-gd
php7.0-bz2 ghostscript graphicsmagick-imagemagick-compat ca-certificates  
  
# Build zbarimg  
WORKDIR /root  
RUN apt-get install -y build-essential libmagick++-dev gettext libtool
autoconf automake  
RUN git clone https://github.com/cmehay/zbar zbarimg --branch=cmehay-patch-1  
WORKDIR zbarimg  
RUN autoreconf --install  
RUN ./configure --with-x=no --with-jpeg=no --enable-video=no --with-python=no
--with-gtk=no --with-qt=no  
RUN make && make install-exec  
  
# Conf nginx  
RUN /bin/sed -i 's/\/app/\/var\/www\/qraidcode\/public/g'
/etc/nginx/host.d/default.conf  
  
WORKDIR /var/www/  
# Clone repository  
RUN git clone https://github.com/cmehay/qraidcode_php.git qraidcode  
  
# Install tFPDF  
RUN git clone https://github.com/rev42/tfpdf.git tfpdf  
RUN chown -R core:core .  
RUN chown -R core:core /var/lib/php  

