FROM debian:jessie  
  
MAINTAINER janes <miscjanes@gmail.com>  
  
# Install program to configure locales  
RUN apt-get update \  
&& apt-get install -y g++ python-pip libyaml-dev python-dev wget \  
&& pip install prettytable Mako PyYAML python-dateutil PySocks --upgrade \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY code/ /opt/weevely/  
  
RUN ln -s /opt/weevely/weevely.py /usr/local/bin/weevely  
  
CMD ["/bin/bash"]  
  

