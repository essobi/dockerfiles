FROM fvigotti/webserver-nginx-php  
  
#ENV PHPMYADMIN_VERSION 4.5.3.1  
ENV PHPMYADMIN_VERSION 4.6.0  
RUN whoami  
  
WORKDIR /  
  
RUN echo "hi"  
RUN wget
https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.bz2
\  
&& tar -xvjf /phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.bz2 -C / \  
&& rm /phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.bz2 \  
&& rsync -a /phpMyAdmin-${PHPMYADMIN_VERSION}-english/ /data/http/  
# && rsync -a /phpMyAdmin-${PHPMYADMIN_VERSION}-english/ /data/pma/ \  
# && rsync -a /phpMyAdmin-${PHPMYADMIN_VERSION}-english/ /pma/  
#RUN ls -laR /data/http/  
#RUN ls -laR /data/  
# add phpmyadmin setup file  
ADD config/* /config/  
ADD data/* /data/  

