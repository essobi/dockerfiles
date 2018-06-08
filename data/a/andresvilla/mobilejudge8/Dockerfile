FROM ubuntu:14.04  
COPY Docker/php.ini /configFiles/  
COPY Docker/mysql_secure.sh /configFiles/  
COPY Docker/mime.types /configFiles/  
COPY Docker/nginx.conf /configFiles/  
COPY Docker/default /configFiles/  
COPY Docker/services.sh /configFiles/  
COPY Code/ /MobileJudge8  
COPY Code/api/ /MobileJudge8  
COPY Docker/sencha_configure.sh /configFiles/  
  
#oauthd  
RUN sudo apt-get update -y  
RUN sudo apt-get upgrade -y  
RUN sudo apt-get dist-upgrade -y  
RUN sudo apt-get install wget -y  
RUN sudo apt-get install nodejs -y  
RUN sudo ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN sudo apt-get install npm -y  
  
RUN sudo apt-get install build-essential -y  
RUN sudo apt-get install tcl8.5 -y  
RUN wget http://download.redis.io/releases/redis-stable.tar.gz && tar xzvf
redis-stable.tar.gz && cd redis-stable && make && make test && sudo make
install && \  
cd utils && ./install_server.sh  
  
RUN rm -rf redis-stable/  
RUN sudo apt-get install git -y  
RUN sudo npm install -g grunt-cli  
  
RUN sudo npm install -g oauthd  
  
RUN sudo oauthd init  
  
EXPOSE 6284  
#mariadb  
RUN sudo apt-get install software-properties-common -y  
RUN sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN sudo add-apt-repository 'deb [arch-amd64, i386]
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu trusty main';
exit 0  
  
RUN sudo apt-get install vim -y  
RUN sudo apt-get install aptitude -y  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y mariadb-server  
  
RUN sudo service mysql start && sudo sh /configFiles/mysql_secure.sh  
  
EXPOSE 13306  
EXPOSE 3306  
#phpmyadmin  
RUN sudo apt-get install php5-fpm php5-mysql php5-mcrypt -y  
  
RUN sudo cp /configFiles/php.ini /etc/php5/fpm/  
  
RUN sudo php5enmod mcrypt  
RUN sudo service php5-fpm restart  
  
RUN sudo apt-get install phpmyadmin -y  
  
#NGINX  
RUN sudo apt-get install nginx -y  
  
RUN sudo cp /configFiles/mime.types /etc/nginx/  
RUN sudo cp /configFiles/nginx.conf /etc/nginx/  
RUN sudo cp /configFiles/default /etc/nginx/sites-enabled/  
  
#link the files in nginx to the repo versions  
RUN sudo ln -s /usr/share/phpmyadmin /usr/share/nginx/html  
  
RUN sudo service apache2 stop  
  
EXPOSE 80  
RUN sudo service nginx restart  
RUN sudo service nginx start  
  
#Sencha Cmd  
RUN apt-get install unzip  
RUN wget http://cdn.sencha.com/cmd/6.0.2/no-jre/SenchaCmd-6.0.2-linux-
amd64.sh.zip -P /  
RUN unzip /SenchaCmd-6.0.2-linux-amd64.sh.zip  
RUN apt-get install default-jre -y  
RUN sh SenchaCmd-6.0.2.14-linux-amd64.sh -q  
  
RUN export PATH="/home/andres/bin/Sencha/Cmd/6.0.2.14/..:$PATH" && sudo sh
/configFiles/sencha_configure.sh  
RUN sudo cp -rf /MobileJudge8/api /usr/share/nginx/html/  
RUN wget -qO- http://install.keymetrics.io/install.sh |
SECRET_ID=c4oqalvhmicddmz PUBLIC_ID=7wu2tbb2eyc6sh1 sudo bash  
RUN sudo pm2 link c4oqalvhmicddmz 7wu2tbb2eyc6sh1 mj.cis.fiu.edu  
RUN sudo pm2 install pm2-server-monit  
RUN sudo pm2 install pm2-mysql  
RUN sudo pm2 install pm2-redis  
RUN sudo pm2 set pm2:passwd Judge2016  
RUN cd /usr/share/nginx/html/api && npm install  
RUN cd /usr/share/nginx/html/api && sudo pm2 start index.js -i 0 --watch
--name "mj-api"  
#RUN cp -rf /MobileJudge8/oauthd /usr/share/nginx/html/  
#RUN cd /usr/share/nginx/html/oauthd && sudo pm2 start index.js -i 0 watch
--name "mj-oauthd" && sudo pm2 save && sudo pm2 startup ubuntu  
RUN sudo apt-get install redis-server -y  
  
RUN mysqladmin -u root password root; exit 0  
  
CMD ["sh", "configFiles/services.sh"]  

