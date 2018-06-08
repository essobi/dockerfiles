# This dockerfile uses the ubuntu image  
# VERSION1  
# Author: frish  
# 基本映像檔，必須是第一個指令  
FROM ubuntu  
  
# 維護者  
MAINTAINER frish <frish@ipair.com>  
  
RUN apt-get update && apt-get install -y nginx  
RUN groupadd -g 80 www && useradd -g www -u 80 -s /bin/false -m www &&
/bin/mkdir -p /export/httpd/project1/htdocs/ && /bin/chown -R www.www
/export/httpd/ && /bin/chown -R www.www /var/lib/nginx  
RUN /usr/sbin/update-rc.d nginx defaults  
  
COPY ./nginx.conf /etc/nginx/  
COPY ./index.html /export/httpd/project1/htdocs/  
  
EXPOSE 80  

