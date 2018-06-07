  
FROM tutum/lamp:latest  
  
RUN apt-get -y update --fix-missing  
RUN apt-get -y install \  
automake \  
bison \  
build-essential \  
curl \  
gawk \  
libffi-dev \  
libgdbm-dev \  
libgmp-dev \  
liblzma-dev \  
libncurses5-dev \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libyaml-dev \  
libtool \  
patch \  
php5-gd \  
pkg-config \  
python \  
python-pip \  
python-setuptools \  
python3 \  
python3-pip \  
python3-setuptools \  
sqlite3 \  
vim \  
wget \  
zlib1g-dev  
  
# Install DVWA  
RUN rm -fr /app && git clone https://github.com/RandomStorm/DVWA /app  
RUN sed -i -e "s/AllowOverride FileInfo/AllowOverride FileInfo Options/"
/etc/apache2/sites-enabled/000-default.conf  
RUN sed -i -e "s/allow_url_include = Off/allow_url_include = On/"
/etc/php5/apache2/php.ini  
RUN sed -i -e 's/root/admin/' /app/config/config.inc.php  
RUN chmod 777 /app/hackable/uploads  
RUN chmod 777 /app/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt  
  
# Install Ruby from source  
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.3.tar.gz  
RUN tar -xzvf ruby-2.3.3.tar.gz \  
&& cd ruby-2.3.3 \  
&& ./configure \  
&& make \  
&& make install  
RUN ruby -v  
  
# Install Fuzzer deps  
RUN gem install mechanize  
RUN pip install requests beautifulsoup4  
RUN pip3 install requests beautifulsoup4  
  
CMD ["/run.sh"]  

