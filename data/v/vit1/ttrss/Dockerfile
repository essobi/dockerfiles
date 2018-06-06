FROM clue/ttrss  
MAINTAINER Vitalii Vokhmin <vitaliy.vokhmin@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y unzip
&& apt-get clean  
  
# install feedly theme  
ADD https://github.com/levito/tt-rss-feedly-theme/archive/master.zip
/tmp/feedly.zip  
RUN unzip /tmp/feedly.zip -d /tmp && \  
cp -rf /tmp/tt-rss-feedly-theme-master/* themes/ && \  
chown -R www-data:www-data themes/  
  
# install videoframes plugin  
ADD https://github.com/tribut/ttrss-videoframes/archive/master.zip
/tmp/video.zip  
RUN unzip /tmp/video.zip -d /tmp && \  
cp -rf /tmp/ttrss-videoframes-master/* plugins/ && \  
chown -R www-data:www-data plugins/  
  
# cleanup /tmp  
RUN rm -rf /tmp/*  
  
# set cookie lifetime to 30 days  
RUN sed -i "s/'SESSION_COOKIE_LIFETIME', 86400/'SESSION_COOKIE_LIFETIME',
2592000/" config.php  

