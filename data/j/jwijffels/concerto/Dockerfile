FROM ubuntu:12.04  
MAINTAINER "Jan Wijffels" jwijffels@bnosac.be  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
## Set a default user  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff \  
&& echo "docker:docker" | chpasswd  
  
WORKDIR /home/docker  
RUN apt-get update -qq && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get update -qq && apt-get install -y --no-install-recommends wget
locales vim-tiny sudo  
  
## Set default locale  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen en_US.utf8 &&
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
## Installation instructions at http://cran.r-project.org/bin/linux/ubuntu/ to
obtain the latest R  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | sudo apt-key add \- \  
&& echo "deb http://cran.at.r-project.org/bin/linux/ubuntu precise/" | tee -a
/etc/apt/sources.list  
  
# Install R  
RUN apt-get update -qq && apt-get -y dist-upgrade && apt-get install -y --no-
install-recommends \  
libc6 \  
file \  
ca-certificates \  
git \  
psmisc \  
libcurl4-openssl-dev \  
software-properties-common \  
libapparmor1 \  
libssl0.9.8 \  
supervisor \  
r-base \  
r-base-dev \  
r-recommended \  
&& wget http://download2.rstudio.org/rstudio-server-0.98.978-amd64.deb \  
&& dpkg -i rstudio-server-0.98.978-amd64.deb \  
&& rm rstudio-server-*-amd64.deb \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds /tmp/* /var/tmp/* \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
## Set CRAN repository  
RUN echo 'options(repos = list(CRAN = "http://cran.at.r-project.org"))' >>
/etc/R/Rprofile.site  
  
## Make a user and a user directory for Rstudio, configure git and set sudo
rights  
## Run supervisord (https://docs.docker.com/articles/using_supervisord/ and
http://supervisord.org/configuration.html) which runs the rstudio server on
port 8787  
RUN mkdir -p /var/log/supervisor  
COPY userconf.sh /usr/bin/userconf.sh  
RUN chmod +x /usr/bin/userconf.sh  
COPY supervisord.conf /etc/supervisord.conf  
EXPOSE 8787  
##  
## Concerto  
##  
## for mysql server popup  
RUN echo mysql-server mysql-server/root_password password abc123 | debconf-
set-selections  
RUN echo mysql-server mysql-server/root_password_again password abc123 |
debconf-set-selections  
## install mysql  
RUN apt-get install -y mysql-server mysql-client mysql-common apache2
libmysqlclient-dev php5 libapache2-mod-php5 php5-mysql \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds /tmp/* /var/tmp/* \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
## Set up the concerto database  
RUN /usr/sbin/mysqld & \  
sleep 10 &&\  
mysql --user=root --password=abc123 -e "create database db_master_name"; \  
mysql --user=root --password=abc123 -e "GRANT ALL PRIVILEGES ON *.* TO
'db_master_user'@'%' IDENTIFIED BY 'db_password' WITH GRANT OPTION;"  
  
## Follow the installation steps of Concerto regarding php settings  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/apache2/php.ini  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/cli/php.ini  
  
## Get concerto  
RUN wget https://concerto-
platform.googlecode.com/files/concerto_platform_v4.0.0.beta8.zip  
RUN mkdir /var/www/concerto  
RUN unzip concerto_platform_v4.0.0.beta8.zip -d /var/www/concerto  
RUN wget
http://cran.r-project.org/src/contrib/Archive/rjson/rjson_0.2.13.tar.gz  
## Install the concerto R package  
RUN R CMD INSTALL rjson_0.2.13.tar.gz --library=/usr/lib/R/library  
RUN R CMD build /var/www/concerto/lib/R/concerto  
RUN R -e "install.packages(c('session', 'RMySQL'), lib =
'/usr/lib/R/library')"  
RUN R CMD INSTALL concerto_0.3.3.tar.gz --library=/usr/lib/R/library  
  
RUN chown -R www-data /var/www/concerto  
RUN chmod -R -v 777 /var/www/concerto  
  
## Expose the MySQL and Apache port  
EXPOSE 3306 80  
## Start up Apache, MySQL and RStudio  
CMD service apache2 start && /usr/bin/mysqld_safe && /usr/bin/supervisord
--configuration=/etc/supervisord.conf  
  

