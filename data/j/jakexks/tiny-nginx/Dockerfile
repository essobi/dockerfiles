FROM scratch  
MAINTAINER Jake Sanders <jake@livewyer.com>  
  
ADD rootfs.tar.gz /  
ADD nginx.conf /etc/nginx/nginx.conf  
  
RUN mkdir /srv && mkdir /srv/website && echo "<h1>It works!</h1>" >
/srv/website/index.html && echo "<?php phpinfo();" > /srv/website/index.php  
  
EXPOSE 80  
CMD ["nginx"]  

