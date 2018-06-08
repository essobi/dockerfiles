FROM globalwolf/app:11.14.2  
ENV DEBIAN_FRONTEND noninteractive  
  
# This line accepts the Microsoft End User License Agreement allowing use of  
# the MS True Type core fonts  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
  
RUN apt-get clean && apt-add-repository multiverse && apt-get update && apt-
get install -y --force-yes \  
build-essential wget gdebi pdftk gearman-job-server gearman-tools ttf-
mscorefonts-installer  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && \  
gdebi --n wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4730  

