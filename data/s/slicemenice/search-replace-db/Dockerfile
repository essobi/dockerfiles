FROM slicemenice/apache-for-wordpress:with-tools  
  
RUN apt-get update && apt-get install -y \  
git \  
libyaml-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pecl install yaml  
  
RUN git clone https://github.com/interconnectit/Search-Replace-DB.git /app  
  
WORKDIR /app  
  
ADD ./srdb.bulk.php ./srdb.bulk.php  
ADD ./php.ini /usr/local/etc/php/php.ini  
  
CMD [ "php" ]

