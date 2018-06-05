FROM ubuntu:trusty  
RUN sed
's&http://archive.ubuntu.com/ubuntu/&mirror://mirrors.ubuntu.com/mirrors.txt&'
-i /etc/apt/sources.list  
COPY . /root/AInstall-master  
WORKDIR /root/AInstall-master  
EXPOSE 9443  
CMD ./install.sh  
#RUN sed 's/SSLEngine on//' -i /etc/apache2/sites-enabled/abills_httpd.conf  
#RUN sed 's/SSLCertificateFile .*//' -i /etc/apache2/sites-
enabled/abills_httpd.conf  
#RUN sed 's/SSLCertificateKeyFile .*//' -i /etc/apache2/sites-
enabled/abills_httpd.conf  
#RUN mkdir -p /var/log/httpd  

