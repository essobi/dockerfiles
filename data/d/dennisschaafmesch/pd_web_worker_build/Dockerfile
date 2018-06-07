FROM ubuntu:xenial  
MAINTAINER Dennis Schaaf <dennis@plantdemand.com>  
  
# Update packages  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update -qq  
RUN apt-get upgrade -y -qq  
  
# Set Locale  
RUN apt-get install -y locales locales-all  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
# Download and install wkhtmltopdf  
RUN apt-get install -y -qq build-essential xorg libssl-dev libxrender-dev wget
libxrender1 fontconfig xvfb gdebi --quiet  
COPY wkhtmltox-0.12.4_linux-generic-amd64.tar.xz /wkhtmltox.tar.xz  
RUN sudo mkdir -p /opt  
RUN cd /opt; sudo tar xf /wkhtmltox.tar.xz  
RUN sudo ln -s /opt/wkhtmltox/bin/wkhtmltopdf /usr/bin/wkhtmltopdf  
  
# Install other important tools  
RUN apt-get install -y -qq git libmysqlclient-dev wget libxml2-dev libxslt-dev
curl  
  
# Python Environment  
RUN apt-get install -y -qq python3-pip python3-dev python-virtualenv  
  
# Install Node 4.x  
RUN apt-get install -y -qq nodejs  
RUN ln -sf /usr/bin/nodejs /usr/bin/node  
  
# Prepare Environment  
COPY docker_entry_point.sh /docker_entry_point.sh  
COPY virtual_env_entry_point.sh /virtual_env_entry_point.sh  
RUN chmod 755 /*.sh  
  
CMD ["/bin/sh", "/docker_entry_point.sh"]  
EXPOSE 80  

