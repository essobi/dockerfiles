FROM weyforth/wordpress-phpcli  
  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y netcat-traditional less mysql-client php5-mysqlnd && \  
update-alternatives --set nc /bin/nc.traditional && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data/www  
COPY wp /usr/local/bin/  
  
ADD https://github.com/wp-cli/wp-cli/releases/download/v0.19.2/wp-
cli-0.19.2.phar /usr/local/bin/wp-cli  
RUN chmod +x /usr/local/bin/wp-cli  
RUN chown www-data:www-data /usr/local/bin/wp  
RUN chown www-data:www-data /usr/local/bin/wp-cli  
  
USER "www-data"  
ENTRYPOINT [ ]  
CMD ["--help"]  

