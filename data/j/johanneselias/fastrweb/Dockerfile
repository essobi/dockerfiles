FROM johanneselias/ubuntu1704-apache2-php-perl:1.1  
RUN echo 'deb http://ftp.gwdg.de/pub/misc/cran/bin/linux/ubuntu zesty/' >>
/etc/apt/sources.list  
  
RUN apt-get -y update && apt-get install -y --allow-unauthenticated \  
libcairo2-dev \  
python3 \  
r-base \  
r-base-dev  
  
RUN Rscript -e "install.packages(c('FastRWeb', 'Rserve', 'XML', 'Cairo',
'Matrix', 'log4r', 'dplyr', 'ggplot2', 'openxlsx'), repos =
'http://ftp.gwdg.de/pub/misc/cran')"  
  
WORKDIR /usr/local/lib/R/site-library/FastRWeb  
RUN ./install.sh \  
chown -R www-data:www-data /var/FastRWeb  
  
WORKDIR /setup  
  
# install copyfiles.py  
RUN wget https://github.com/joheli/copyfiles/archive/v0.6.tar.gz; \  
tar -xzf v0.6.tar.gz; \  
chmod 755 /setup/copyfiles-0.6/copyfiles.py; \  
ln -s /setup/copyfiles-0.6/copyfiles.py /usr/bin/  
  
WORKDIR /var/www  
  
RUN cp /usr/local/lib/R/site-library/FastRWeb/cgi-bin/Rcgi /usr/lib/cgi-bin/R  
  
COPY helper/fastrweb-configure /usr/bin/  
  
RUN chmod 700 /usr/bin/fastrweb-configure; \  
chmod -R 755 /usr/lib/cgi-bin  
  
ENTRYPOINT ["fastrweb-configure"]  
  

