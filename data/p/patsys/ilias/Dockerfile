FROM patsys/apache  
MAINTAINER Patrick Weber <pat.weber91@gmail.com>  
COPY 25_ilias_setup.sh /etc/my_init.d/  
RUN chmod u+x /etc/my_init.d/25_ilias_setup.sh  
RUN apk update && apk upgrade && apk add sudo coreutils openssl lynx zip unzip
imagemagick ghostscript mysql-client php5-json php5-xml php5-dom php5-gd
php5-xsl php5-mysqli php5-mysql php5-iconv ca-certificates && rm -rf
/var/cache/apk/*  
RUN update-ca-certificates  
CMD ["/etc/start"]  

