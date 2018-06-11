FROM openlabs/tryton:3.2  
MAINTAINER Umang Arora <umang.arora@openlabs.co.in>  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install dependencies for wkhtmltopdf  
RUN apt-get install -y openssl build-essential xorg libssl-dev libxrender-dev
wget xvfb git-core fontconfig curl  
  
# Install wkhtmltopdf 0.12.1 stable  
RUN wget
http://citylan.dl.sourceforge.net/project/wkhtmltopdf/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb  
RUN dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb  

