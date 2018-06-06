FROM fedora:25  
MAINTAINER Andrae Findlator <andrae.findlator@gmail.com>  
  
RUN dnf update -y && dnf install -y php php-ssh2 php-pdo php-pdo-dblib php-xml
php-mbstring php-bcmath unzip  
  
COPY ./app /Worker/  
  
WORKDIR "/Worker"  
  
ENTRYPOINT ["/Worker/rolldata2.sh"]  

