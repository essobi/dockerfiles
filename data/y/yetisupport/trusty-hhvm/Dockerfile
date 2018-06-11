FROM ubuntu:trusty  
  
VOLUME /var/lib/hhvm/sessions  
  
RUN apt-get install -y software-properties-common  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN add-apt-repository -y "deb http://dl.hhvm.com/ubuntu trusty-lts-3.9 main"  
RUN apt-get update -y  
RUN apt-get install -y hhvm nginx  
  
ADD nginx /etc/nginx  
ADD hhvm/server.ini /etc/hhvm/server.ini  
ADD hhvm/php.ini /etc/hhvm/php.ini  
ADD index.php /var/www/app/public/index.php  
ADD run.sh /var/www/run.sh  
  
RUN rm -f /var/log/nginx/access.log; ln -s /dev/stdout
/var/log/nginx/access.log  
RUN rm -f /var/log/nginx/error.log; ln -s /dev/stderr /var/log/nginx/error.log  
  
WORKDIR /var/www/app  
EXPOSE 80  
CMD /var/www/run.sh  

