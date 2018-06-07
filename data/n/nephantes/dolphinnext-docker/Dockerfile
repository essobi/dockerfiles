FROM ubuntu:latest  
  
MAINTAINER Alper Kucukural <alper.kucukural@umassmed.edu>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get dist-upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 \  
php-pear curl lynx-cur mysql-server \  
libreadline-dev libsqlite3-dev libbz2-dev libssl-dev python python-dev \  
libmysqlclient-dev python-pip git expect default-jre \  
libxml2-dev software-properties-common gdebi-core wget \  
tree vim libv8-dev subversion g++ gcc gfortran zlib1g-dev libreadline-dev \  
libx11-dev xorg-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-openssl-dev  
  
RUN apt-get clean  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-
properties  
RUN LC_ALL=C.UTF-8 apt-add-repository ppa:ondrej/php  
RUN apt-get update  
RUN apt-get -y install php7.2  
RUN apt-get -y install php-pear php7.2-curl php7.2-dev php7.2-gd
php7.2-mbstring php7.2-zip php7.2-mysql php7.2-xml  
RUN apt-get install -y ssh openssh-server  
  
# Enable apache mods.  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.2/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php/7.2/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf  
RUN a2enconf fqdn  
  
RUN echo "locale-gen en_US.UTF-8"  
RUN echo "dpkg-reconfigure locales"  
  
# Copy site into place.  
ENV GITUSER=UMMS-Biocore  
ADD bin /usr/local/bin  
  
RUN git clone https://github.com/${GITUSER}/biocorepipe.git
/var/www/html/biocorepipe  
RUN chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /var/www/html/biocorepipe  
  
RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && \  
mysql -u root -e 'CREATE DATABASE biocorepipe;' && \  
cat /var/www/html/biocorepipe/db/biocorepipe.sql|mysql -uroot biocorepipe && \  
cd /var/www/html/biocorepipe/db && ./runUpdate biocorepipe && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:nijel/phpmyadmin && \  
service apache2 start && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install phpmyadmin && \  
zcat /usr/share/doc/phpmyadmin/examples/create_tables.sql.gz|mysql -uroot  
  
RUN usermod -d /var/lib/mysql/ mysql  
  
RUN sed -i "s#// \$cfg\\['Servers'\\]\\[\$i\\]\\['AllowNoPassword'\\] =
TRUE;#\$cfg\\['Servers'\\]\\[\$i\\]\\['AllowNoPassword'\\] = TRUE;#g"
/etc/phpmyadmin/config.inc.php  
RUN ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-
enabled/phpmyadmin.conf  
  
RUN apt-get -y autoremove  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN curl -s https://get.nextflow.io | bash  
RUN mv /data/nextflow /usr/bin/.  
RUN chmod 755 /usr/bin/nextflow  
  
RUN wget https://phar.phpunit.de/phpunit-7.0.2.phar  
RUN chmod +x phpunit-7.0.2.phar  
RUN mv phpunit-7.0.2.phar /usr/local/bin/phpunit  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.4.10-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN conda update -n base conda  
RUN conda config --add channels bioconda  
RUN conda install -y -c bioconda tophat  
  
RUN echo "DONE!"  
  

