  
# Start from my base image  
FROM pjzz/base  
  
# add the namecoin repo  
RUN wget
http://download.opensuse.org/repositories/home:p_conrad:coins/Debian_7.0/Release.key
-O - | apt-key add -  
RUN echo 'deb
http://download.opensuse.org/repositories/home:/p_conrad:/coins/Debian_7.0/ /'
>> /etc/apt/sources.list.d/namecoin.list  
RUN apt-get update # 20140326  
  
# install namecoin, bind, and NamecoinToBind deps  
RUN apt-get install -y bind9 idn php5-cli git namecoin cron ssmtp git ; apt-
get clean  
  
# configure namecoin  
WORKDIR /root  
RUN mkdir -p .namecoin  
#ADD namecoin.conf /.namecoin/  
RUN echo "rpcuser=root" >>.namecoin/namecoin.conf  
RUN echo "rpcpassword=longhardpassword" >>.namecoin/namecoin.conf  
RUN echo "rpcport=8336" >>.namecoin/namecoin.conf  
  
# install NamecoinToBind  
WORKDIR /home  
RUN mkdir -p NamecoinToBind  
ADD NamecoinToBind.tar.gz /home/NamecoinToBind/  
RUN cp NamecoinToBind/etc/bind/named.conf.bit /etc/bind/named.conf.d ;\  
mkdir -p /etc/bind/dotbit/ ;\  
chown -R www-data:www-data /etc/bind/dotbit ;\  
cp NamecoinToBind/etc/cron.d/namecoinToBind /etc/cron.d/ ;\  
mkdir -p NamecoinToBind/cache NamecoinToBind/stat ;\  
chown -R www-data:www-data NamecoinToBind/cache NamecoinToBind/stat  
ADD config.php /home/NamecoinToBind/config.php  
RUN perl -pi -e"s/username/root/" NamecoinToBind/config.php # insert username  
RUN perl -pi -e"s/password/longhardpassword/" NamecoinToBind/config.php #
insert password  
RUN perl -pi -e"s/hostname/localhost.localdomain/" NamecoinToBind/config.php #
insert hostname  
  
# expose the dns port  
EXPOSE 53  
# Add our supervisor config  
ADD namecoindns.conf /etc/supervisor/conf.d/  
CMD supervisord -c /etc/supervisor.conf  
  

