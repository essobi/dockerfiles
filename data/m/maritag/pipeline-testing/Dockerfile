FROM webdevops/php-apache-dev:5.6  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN apt-get update; apt-get install -y jq unzip  
RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-
scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip  
RUN unzip sonar-scanner-cli-3.2.0.1227-linux.zip  
RUN export SONAR_SCANNER_OPTS="-Xmx1024m"  
ENV PATH="${PATH}:/sonar-scanner-3.2.0.1227-linux/bin"  

