FROM python:3.6  
MAINTAINER Jesse Butterfield "jesse@semprehealth.com"  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Download and install wkhtmltopdf  
RUN apt-get install -y wget  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN mv wkhtmltox/bin/wkhtmlto* /usr/bin/  

