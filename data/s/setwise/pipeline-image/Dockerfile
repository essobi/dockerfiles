# Extension of an exsiting laravel/homestead comapatable image to includ
mysql.  
FROM ubuntu:16.04  
## Install mysql and add homestead user.  
## Note: since this is only for testing, the mysql root user is left without
password.  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' && \  
apt-get update  
RUN echo 'mysql-server mysql-server/root_password password root' | debconf-
set-selections && \  
echo 'mysql-server mysql-server/root_password_again password root' | debconf-
set-selections && \  
apt-get -y install mysql-server-5.6 mysql-client-5.6  
RUN service mysql start && \  
mysql -uroot -proot -e "CREATE USER 'homestead'@'localhost' IDENTIFIED BY
'secret';" && \  
mysql -uroot -proot -e "GRANT ALL PRIVILEGES ON *.* TO
'homestead'@'localhost';"  
  
# Install nodejs and npm using ("n" for node version control) then some useful
packages  
RUN apt-get -y install wget curl git nodejs npm libpng-dev  
RUN npm install -g n && \  
n 8.9.0 && \  
npm config set unsafe-perm true && \  
npm config set user 0 && \  
npm install -g flightplan gulp  
  
ADD files/package.json /opt/files/package.json  
RUN npm --prefix /opt/files install  
  
# Install php and composer  
RUN apt-get -y install php7.0-cli php7.0-fpm php7.0-opcache php7.0-mbstring
php7.0-mysql php7.0-xml php7.0-gd php7.0-curl php7.0-zip php7.0-pgsql  
  
ADD scripts/composer_install.sh /composer_install.sh  
RUN chmod +x /composer_install.sh  
RUN /composer_install.sh && \  
mv /tmp/composer.phar /usr/local/bin/composer  
  
## Install Java8  
RUN apt-get install -y openjdk-8-jre openjdk-8-jdk xvfb unzip git dbus  
  
# Install chrome and chromedriver  
RUN curl -L -o /tmp/chrome.deb https://dl.google.com/linux/direct/google-
chrome-stable_current_amd64.deb && \  
apt-get update && \  
dpkg -i /tmp/chrome.deb || apt-get -y -f install  
RUN curl -L -o /tmp/chromedriver.zip
https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && \  
unzip /tmp/chromedriver.zip -d /tmp/ && \  
chmod +x /tmp/chromedriver && \  
mv /tmp/chromedriver /usr/local/bin/  
  
# Install Selenium server.  
RUN curl -o /tmp/selenium.jar https://selenium-
release.storage.googleapis.com/3.8/selenium-server-standalone-3.8.1.jar && \  
mv /tmp/selenium.jar /usr/local/bin/  
  
# Install PostgreSQL  
RUN apt-get -y install postgresql postgresql-contrib  
RUN useradd homestead && \  
echo homestead:secret | chpasswd && \  
service postgresql start && \  
su - postgres -s /bin/bash -c "createuser -s root" && \  
createuser -s homestead && \  
psql -c "ALTER USER homestead WITH PASSWORD 'secret'" -d postgres  
  
# Install Postgis extension  
RUN add-apt-repository -y ppa:ubuntugis/ppa && \  
apt-get update && \  
apt-get -y install postgis  
  
ADD scripts/start.sh /start.sh  
ADD scripts/profile.sh /root/.profile  
ADD scripts/profile.sh /root/.bash_rc  
ADD scripts/entrypoint.sh /opt/scripts/entrypoint.sh  
  
RUN chmod +x /opt/scripts/entrypoint.sh /root/.profile /root/.bash_rc
/start.sh  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

