FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install PHP  
RUN apt-get update \  
&& apt-get install -y \  
php7.0 \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-mcrypt \  
php7.0-mysql \  
curl \  
php-pear \  
php7.0-dev \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install MSSQL for PHP  
RUN \  
#####################################  
# Ref from https://github.com/Microsoft/msphpsql/wiki/Dockerfile-for-adding-
pdo_sqlsrv-and-sqlsrv-to-official-php-image  
#####################################  
# Add Microsoft repo for Microsoft ODBC Driver 13 for Linux  
apt-get update -yqq && apt-get install -y apt-transport-https \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl https://packages.microsoft.com/config/debian/8/prod.list >
/etc/apt/sources.list.d/mssql-release.list \  
&& apt-get update -yqq \  
  
# Install Dependencies  
&& ACCEPT_EULA=Y apt-get install -y unixodbc unixodbc-dev libgss3 odbcinst
msodbcsql locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen \  
  
# Install pdo_sqlsrv and sqlsrv from PECL. Replace pdo_sqlsrv-4.1.8preview
with preferred version.  
&& pecl install pdo_sqlsrv-4.1.8preview sqlsrv-4.1.8preview \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update \  
&& apt-get install apache2 libapache2-mod-php7.0 -y \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update \  
&& apt-get install mariadb-common mariadb-server mariadb-client -y \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update \  
&& apt-get install -y git nano tree sudo dnsmasq dnsutils supervisor iputils-
ping unzip \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /var/log/supervisor  
RUN sudo /bin/su -c "echo \"user=root\" >> /etc/dnsmasq.conf"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates socat \  
&& apt-get install -y --no-install-recommends xvfb x11vnc fluxbox xterm \  
&& apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable \  
&& apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /usr/bin  
  
#RUN curl -O
https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip  
#RUN unzip chromedriver_linux64.zip  
#RUN chmod +x chromedriver  
#INSTALL NPM  
  
RUN apt-get update && apt-get install -y php7.0-mbstring php7.0-zip && apt-get
clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
ENV NVM_DIR /root/.nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install stable \  
&& nvm install 7.5 \  
&& nvm use stable \  
&& nvm alias stable  
  
RUN echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& sudo apt-get update && sudo apt-get install yarn -y \  
&& apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/www  
  
VOLUME /dev/shm  
  
WORKDIR /var/www  
  
EXPOSE 80 9515 5900 3306  
# COPY SCRIPTS  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY . /usr/sbin  
RUN chmod +x /usr/sbin/docker-php-ext-enable  
RUN /usr/sbin/docker-php-ext-enable pdo_sqlsrv sqlsrv  
RUN chmod +x /usr/sbin/entry_point.sh  
COPY entry_point.sh /usr/bin/boot_services  
RUN chmod +x /usr/bin/boot_services  
  
CMD ["/bin/sh", "-c", "/usr/sbin/entry_point.sh > /var/www/boot.log"]

