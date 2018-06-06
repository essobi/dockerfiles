FROM quay.io/actcat/buildpack_php:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
RUN apt-get update -y && apt-get install -y unzip  
  
# Install PHP_CodeSniffer from http://pear.php.net/package/PHP_CodeSniffer/  
RUN pear install PHP_CodeSniffer-2.5.0  
  
# set codesniffer of cakephp  
RUN wget https://github.com/cakephp/cakephp-codesniffer/archive/master.zip  
RUN unzip master.zip  
RUN mv cakephp-codesniffer-master/CakePHP
/usr/share/php/PHP/CodeSniffer/Standards/  
RUN rm -rf master.zip cakephp-codesniffer-master/  
  
# set codesniffer of codeigniter  
RUN wget https://github.com/thomas-ernest/CodeIgniter-for-
PHP_CodeSniffer/archive/master.zip  
RUN unzip master.zip  
RUN mv CodeIgniter-for-PHP_CodeSniffer-master/src
/usr/share/php/PHP/CodeSniffer/Standards/CodeIgniter  
RUN rm -rf master.zip CodeIgniter-for-PHP_CodeSniffer-master/  
  
# Install Symfony2 codingstandard for phpcs  
RUN wget https://github.com/escapestudios/Symfony2-coding-
standard/archive/master.zip  
RUN unzip master.zip  
RUN mv Symfony2-coding-standard-master
/usr/share/php/PHP/CodeSniffer/Standards/Symfony  
RUN rm master.zip  
  
# Install fuelphp codingstandard for phpcs  
RUN wget https://github.com/eviweb/fuelphp-phpcs/archive/master.zip  
RUN unzip master.zip  
RUN mv fuelphp-phpcs-master/Standards/FuelPHP
/usr/share/php/PHP/CodeSniffer/Standards/  
RUN rm -rf master.zip fuelphp-phpcs-master/  
  
# Install WordPress Coding Standards for phpcs  
RUN wget https://github.com/WordPress-Coding-Standards/WordPress-Coding-
Standards/archive/master.zip  
RUN unzip master.zip  
RUN mv WordPress-Coding-Standards-master
/usr/share/php/PHP/CodeSniffer/Standards/wpcs  
RUN rm master.zip  
  
# Show a list of installed coding standards  
RUN phpcs -i  
RUN phpcs --version  

