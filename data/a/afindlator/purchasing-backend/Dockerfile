FROM fedora:25  
MAINTAINER Andrae Findlator <andrae.findlator@gmail.com>  
  
RUN dnf update -y && dnf install -y php php-pdo php-pdo-dblib php-mysqlnd php-
xml php-mbstring php-bcmath nodejs  
  
COPY ./app /dr/app  
COPY ./api /dr/api  
  

