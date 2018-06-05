FROM debian:jessie  
  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
ENV SERVER_PORT 80  
ENV SERVER_API_KEY dummy  
ENV WKHTMLTOPDF_BIN "/usr/local/bin/wkhtmltopdf"  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
build-essential \  
libssl-dev \  
libxrender-dev \  
wget \  
gdebi \  
git \  
nodejs-legacy \  
npm  
  
WORKDIR /tmp  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb && \  
gdebi --n wkhtmltox-0.12.2.1_linux-jessie-amd64.deb && \  
rm wkhtmltox-0.12.2.1_linux-jessie-amd64.deb  
  
WORKDIR /  
RUN git clone https://github.com/yappabe/wkhtmltopdf-aas.git  
WORKDIR /wkhtmltopdf-aas  
RUN npm install  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
COPY settings.yml /wkhtmltopdf-aas/config/settings.yml  
  
EXPOSE 80  
CMD ["/run.sh"]

