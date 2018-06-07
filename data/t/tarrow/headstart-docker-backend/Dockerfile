FROM php:7.0-apache  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys
E19F5F87128899B192B1A2C2AD5F960A256A04AF && \  
echo "deb http://cran.us.r-project.org/bin/linux/debian jessie-cran34/" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
sqlite3 \  
libsqlite3-dev \  
r-base \  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev  
RUN docker-php-ext-install pdo_sqlite  
RUN a2enmod headers && service apache2 restart  
ADD installpackages.R /tmp/  
RUN /usr/bin/Rscript /tmp/installpackages.R  
RUN R -e 'devtools::install_github("sckott/ropenaire")'  
RUN R -e 'install.packages("rAltmetric",
repos="http://cran.us.r-project.org")'  
RUN R -e 'install.packages("readr", repos="http://cran.us.r-project.org")'  
RUN R -e 'install.packages("remotes", repos="http://cran.us.r-project.org")'  
RUN R -e 'remotes::install_github("ropensci/rcrossref@async")'  
COPY ./apache2.conf /etc/apache2/apache2.conf  
EXPOSE 80  

