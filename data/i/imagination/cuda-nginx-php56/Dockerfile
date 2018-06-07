FROM imagination/cuda-baseimage-docker:cuda-75  
# Phusion setup  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
# Nginx-PHP Installation  
RUN apt-get update -y && apt-get install -y vim curl wget build-essential
python-software-properties git-core unzip \  
pkg-config python-pip python-dev gfortran libopenblas-dev liblapack-dev
libpng-dev libfreetype6-dev libjpeg-dev libhdf5-dev  
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 4F4EA0AAE5267A6C  
RUN add-apt-repository -y ppa:ondrej/php5-5.6 && add-apt-repository -y
ppa:nginx/stable && add-apt-repository -y ppa:mc3man/trusty-media  
RUN apt-get update -y && sudo apt-get upgrade -y && apt-get install -yq php5
php5-cli php5-fpm php5-mysqlnd \  
php5-pgsql php5-curl php5-gd php5-mcrypt php5-intl php5-imap php5-tidy \  
php-pear php5-xmlrpc newrelic-php5 ffmpeg imagemagick php5-imagick php5-dev
nginx-full ntp -y  
  
# Update PHP timezone database  
RUN pecl install timezonedb  
  
# Run update timezone replace city with relevant city. eg. "Australia/Sydney"  
RUN cp -p /usr/share/zoneinfo/Australia/Sydney /etc/localtime  
  
# Add Chainer to Installation for Neural Styling  
ENV LIBRARY_PATH /usr/local/cuda-7.5/targets/x86_64-linux/lib/stubs  
RUN pip install -U setuptools && pip install -U pip  
RUN pip install chainer==1.6.2.1 Cython==0.23.4 h5py==2.5.0  
RUN pip install image && pip install awscli --ignore-installed six  
  
# Add build script  
RUN mkdir -p /root/setup  
ADD build/setup.sh /root/setup/setup.sh  
RUN chmod +x /root/setup/setup.sh  
RUN (cd /root/setup/; /root/setup/setup.sh)  
  
# Copy files from repo  
ADD build/default /etc/nginx/sites-available/default  
ADD build/nginx.conf /etc/nginx/nginx.conf  
ADD build/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD build/www.conf /etc/php5/fpm/pool.d/www.conf  
ADD build/.bashrc /root/.bashrc  
  
# Add startup scripts for services  
ADD build/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
ADD build/phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
ADD build/ntp.sh /etc/service/ntp/run  
ADD build/ntp.conf /etc/ntp.conf  
RUN chmod +x /etc/service/ntp/run  
  
# Set WWW public folder  
RUN mkdir -p /var/www/public  
ADD build/index.php /var/www/public/index.php  
  
RUN chown -R www-data:www-data /var/www  
RUN chmod -R 755 /var/www  
  
# Add New Relic APM install script  
RUN mkdir -p /etc/my_init.d  
ADD build/newrelic.sh /etc/my_init.d/newrelic.sh  
RUN chmod +x /etc/my_init.d/newrelic.sh  
  
# Setup environment variables for initializing New Relic APM  
ENV NR_INSTALL_SILENT 1  
ENV NR_INSTALL_KEY **ChangeMe**  
ENV NR_APP_NAME "Docker PHP Application"  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install Node Version Manager and install node specific version  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 0.12.10  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  
  
# Set terminal environment  
ENV TERM=xterm  
  
# Port and settings  
EXPOSE 80  
# Cleanup apt and lists  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

