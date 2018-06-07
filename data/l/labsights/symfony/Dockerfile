FROM labsights/base  
MAINTAINER Sorin Badea <sorin@labsights.com>  
  
EXPOSE 80  
#--------------- add the playbook and run it -------------------  
ADD bootstrap.yml /tmp/bootstrap.yml  
ADD templates /tmp/templates  
  
RUN ansible-playbook /tmp/bootstrap.yml  
  
#------------------------- cleanup -----------------------------  
RUN rm -rf /tmp/bootstrap.yml;rm -rf /tmp/templates;  
RUN apt-get autoremove -y;apt-get autoclean -y;apt-get clean -y;  

