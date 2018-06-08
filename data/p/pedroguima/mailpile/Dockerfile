FROM ubuntu:14.04  
MAINTAINER pguimaraes  
  
RUN apt-get update; apt-get install -y zlib1g-dev git gnupg openssl python-
virtualenv python-pip python-lxml python-dev libjpeg-dev  
  
WORKDIR /opt  
  
RUN git clone \--recursive https://github.com/mailpile/Mailpile.git; cd
Mailpile; virtualenv -p /usr/bin/python2.7 --system-site-packages mp-
virtualenv && . mp-virtualenv/bin/activate && pip install -r requirements.txt  
  
ADD start_mailpile.sh .  
  
ENTRYPOINT /opt/start_mailpile.sh  
  
EXPOSE 33411  

