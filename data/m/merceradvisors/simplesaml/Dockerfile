FROM tutum/apache-php  
MAINTAINER Lucid Programmer <lucidprogrammer@hotmail.com>  
# mcrypt and ldap needed for saml to work & adding php5-pgsql for use if the
container to be used for Idp  
RUN apt-get update && apt-get install -y \  
php5-mcrypt \  
php5-ldap \  
php5-pgsql && php5enmod mcrypt  
# Get a fresh copy of simplesamlphp from simplesamlphp.org  
# move contents of simplesamlphp to ./saml, just for clarity  
  
RUN curl -L
https://github.com/simplesamlphp/simplesamlphp/releases/download/v1.14.8/simplesamlphp-1.14.8.tar.gz
> simplesamlphp-1.14.8.tar.gz  
RUN tar xzf simplesamlphp-1.14.8.tar.gz && rm -rf simplesamlphp-1.14.8.tar.gz
&& mv ./simplesamlphp-1.14.8 ./saml  
  
# lets add the alias  
# specific for heroku, listens on all ports.  
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf  
# heroku change for run.sh as heroku will run it with a user who is not apache  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
# for heroku, use $PORT as per their documentation
https://devcenter.heroku.com/articles/container-registry-and-runtime  
ADD ports.conf /etc/apache2  

