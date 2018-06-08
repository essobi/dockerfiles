FROM codeship/google-cloud-deployment  
MAINTAINER Geoffroy Lesage "geoffroy@starchup.com"  
RUN apt-get update  
RUN apt-get install curl python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install nodejs git -y  
  
CMD ["/bin/sh"]

