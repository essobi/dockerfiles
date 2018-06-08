From romeohua/simple-php7:novolume  
  
ENV BASEDIR /data/www  
  
ENV PHPMYADMIN_VERSION 4.6.1  
WORKDIR ${BASEDIR}  
  
RUN rm -rf *  
  
RUN yum -y update && yum install -y curl && yum clean all  
RUN curl -L -o phpmyadmin.tar.gz
"https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-
languages.tar.gz" && \  
tar -xvzf phpmyadmin.tar.gz && \  
mv phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages/* . && \  
rm -rf phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages && \  
rm -f phpmyadmin.tar.gz  
  
RUN chown -R www:www ${BASEDIR}  
  
ADD config.inc.php ${BASEDIR}/config.inc.php

