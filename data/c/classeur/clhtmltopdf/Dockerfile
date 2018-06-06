FROM ubuntu:14.04  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y xorg wget gdebi nodejs npm fonts-freefont* fonts-dejavu
fonts-arphic* ttf-kochi* fonts-baekmuk*  
  
RUN wget
http://downloads.sourceforge.net/project/wkhtmltopdf/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb \  
&& gdebi --n wkhtmltox-0.12.2.1_linux-trusty-amd64.deb \  
&& rm wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm install  
CMD [ "nodejs", "server.js" ]  
  
EXPOSE 3000  

