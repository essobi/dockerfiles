  
FROM mirrored1976/hhvm  
  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"  
RUN apt-get update \  
&& apt-get install -y hhvm  
  
ADD start.sh /  
RUN chmod 755 start.sh \  
&& echo '<?php phpinfo(); ?>' >> /app/phpinfo.php  
  
EXPOSE 9000  
CMD ["/start.sh"]  

