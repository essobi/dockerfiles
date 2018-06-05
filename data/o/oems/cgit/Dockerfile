FROM ubuntu:14.04  
MAINTAINER OEMS <oscaremu@gmaiil.com>  
  
RUN apt-get update && \  
apt-get install -y curl wget supervisor xz-utils build-essential autoconf
automake libtool libssl-dev highlight python-markdown apache2 openssh-server  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CGIT_VERSION 1.0  
ENV MD5_CHECKSUM 1dbd155da1c4adc89703fb1faf249dff  
  
ADD "https://git.zx2c4.com/cgit/snapshot/cgit-$CGIT_VERSION.tar.xz"
/root/cgit/  
  
RUN mkdir -p /root/cgit \  
&& cd /root/cgit \  
&& echo "$MD5_CHECKSUM cgit-$CGIT_VERSION.tar.xz" | md5sum -c - \  
&& tar xf "cgit-$CGIT_VERSION.tar.xz" \  
&& cd "cgit-$CGIT_VERSION" \  
&& make get-git && make && make install \  
&& sed -i '118 s/^/#/' /usr/local/lib/cgit/filters/syntax-highlighting.sh \  
&& echo 'exec highlight --force --inline-css -f -I -O xhtml -S "$EXTENSION"
2>/dev/null' >> /usr/local/lib/cgit/filters/syntax-highlighting.sh  
  
ADD cgit.conf /etc/apache2/sites-available/cgit.conf  
ADD cgitrc /etc/cgitrc  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN a2enmod rewrite && a2enmod cgi \  
&& cd /etc/apache2/mods-enabled \  
&& ln -s ../mods-available/cgi.load cgi.load \  
&& rm /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /etc/apache2/sites-available/cgit.conf /etc/apache2/sites-enabled/  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

