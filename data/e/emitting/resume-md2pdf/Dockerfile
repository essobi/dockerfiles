# use the ubuntu base image provided by official repo  
FROM ubuntu:latest  
MAINTAINER Steve Zhang "stevzhg@gmail.com"  
# prepare work directory  
WORKDIR /resume  
  
# install requirement  
RUN apt-get update  
RUN apt-get install -y git wget python-pip python-dev  
RUN apt-get install -y gdebi-core  
  
# add chinese font support  
RUN apt-get install -y fonts-wqy-zenhei  
  
# install wkhtmltopdf  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb \  
&& gdebi -n wkhtmltox-0.12.2.1_linux-trusty-amd64.deb \  
&& rm wkhtmltox-0.12.2.1_linux-trusty-amd64.deb\  
&& apt-get clean  
  
# install md2pdf  
RUN pip install git+git://github.com/hit9/md2pdf.git@master

