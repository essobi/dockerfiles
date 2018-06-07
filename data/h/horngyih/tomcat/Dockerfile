FROM horngyih/tomcat:7-production  
  
RUN apt-get update  
RUN apt-get install xvfb -y  
RUN apt-get install libxrender1 -y  
RUN apt-get install xfonts-base -y  
RUN apt-get install xfonts-75dpi -y  
RUN apt-get install fontconfig -y  
WORKDIR /tmp  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
WORKDIR /tmp/wkhtmltox/bin/  
RUN mv wkhtmltopdf /usr/bin/wkhtmltopdf  
RUN mv wkhtmltoimage /usr/bin/wkhtmltoimage  
RUN chmod a+x /usr/bin/wkhtmltopdf  
RUN chmod a+x /usr/bin/wkhtmltoimage  
RUN echo 'xvfb-run --server-args="-screen 0, 1920x1080x24"
/usr/bin/wkhtmltopdf $*' > /usr/bin/wkhtmltopdf.sh  
RUN chmod a+rx /usr/bin/wkhtmltopdf.sh  
RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/sbin/wkhtmltopdf  
RUN rm /tmp/*.tar.gz  
  
WORKDIR /usr/local/tomcat  

