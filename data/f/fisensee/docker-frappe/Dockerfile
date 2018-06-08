FROM ubuntu:16.04  
  
RUN useradd frappe && usermod -aG sudo frappe && mkdir /home/frappe && chown
-R frappe.frappe /home/frappe  
  
RUN apt-get update && apt-get install -y build-essential;  
  
WORKDIR /home/frappe  
  
COPY nodejs-install.sh /  
  
RUN bash /nodejs-install.sh  
  
COPY redis-install.sh /  
  
RUN bash /redis-install.sh  
  
RUN apt-get install -y wkhtmltopdf  
  
COPY mariadb-install.sh /  
  
RUN bash /mariadb-install.sh  
  
COPY bench-install.sh /  
  
RUN apt-get install -y python-dev python-setuptools python-mysqldb git \  
ntp vim screen htop \  
libxslt1.1 libxslt1-dev libssl-dev libcrypto++-dev postfix nginx \  
supervisor python-pip fontconfig libxrender1 libxext6 xfonts-75dpi xfonts-base  
  
RUN chmod a+rwx -R /usr/local/  
  
RUN bash /bench-install.sh  
  
EXPOSE 8000  
  
# VOLUME ["/var/lib/mysql", "/home/frappe/frappe-bench/sites/site1.local"]  
# CMD ["/usr/bin/supervisord", "-n"]

