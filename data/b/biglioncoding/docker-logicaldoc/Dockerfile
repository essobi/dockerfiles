FROM cloudesire/tomcat:8-jre8  
MAINTAINER Big Lion <biglion.coding@gmail.com>  
  
RUN sed -i "s/httpredir\\.debian\\.org/ftp.us.debian.org/g"
/etc/apt/sources.list \  
&& apt-get -yqq update \  
&& apt-get -yqq install \  
wget imagemagick ghostscript pdftohtml tesseract-ocr openssl clamav  
  
RUN wget
https://sourceforge.net/projects/logicaldoc/files/distribution/LogicalDOC%20CE%207.5/logicaldoc-
webapp-7.5.1.war \  
&& mv logicaldoc-webapp-7.5.1.war /tomcat/webapps  
  
RUN mkdir /documents  
  
VOLUME ["/documents"]  
  
EXPOSE 8080  
CMD ["/run.sh"]  

