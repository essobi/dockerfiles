FROM fedora:24  
MAINTAINER Andrae Findlator <andrae.findlator@gmail.com>  
  
RUN dnf update -y && dnf install -y vim php php-mssql php-mysql php-xml php-
mbstring php-bcmath  
  
COPY ./ /Worker/  
COPY ./Code/ /Worker/Code/  
  
ENTRYPOINT ["/Worker/worker.php"]  
  

