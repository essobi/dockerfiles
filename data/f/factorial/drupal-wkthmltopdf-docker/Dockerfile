FROM factorial/drupal-docker:php-56  
MAINTAINER stephan@factorial.io  
  
RUN apt-get update && apt-get install -y wget xfonts-base xfonts-75dpi pdftk
xz-utils  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN cp wkhtmltox/bin/wkhtmltopdf /usr/bin  
RUN cp wkhtmltox/lib/* /usr/lib  
  

