FROM ubuntu  
ADD php-fcgi /etc/init.d/php-fcgi  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && \  
apt-get install -y nginx nginx-extras mono-devel mono-complete mono-fastcgi-
server4 php5 php5-cgi spawn-fcgi libc6-dev && \  
chmod 755 /etc/init.d/php-fcgi && \  
/usr/bin/apt-get -y purge git php5-dev libpcre3-dev gcc make && apt-get -y
autoremove && apt-get clean  
  
ADD init.sh /etc/init.sh  
ADD monoserver.sh /etc/init.d/monoserver.sh  
ADD default /etc/nginx/sites-available/default  
ADD default-ssl /etc/nginx/sites-enabled/default-ssl  
ADD fastcgi_params /etc/nginx/fastcgi_params  
ADD server.crt /etc/nginx/ssl/  
ADD server.key /etc/nginx/ssl/  
  
RUN chmod +x /etc/init.sh && chmod +x /etc/init.d/monoserver.sh  
  
EXPOSE 80 443  
CMD /etc/init.sh && /etc/init.d/nginx start && /etc/init.d/monoserver.sh start

