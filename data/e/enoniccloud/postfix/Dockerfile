FROM ubuntu:14.04  
MAINTAINER Erik Kaareng-Sunde <esu@enonic.com>  
  
  
  
  
RUN echo postfix postfix/main_mailer_type string Internet site | debconf-set-
selections  
RUN echo postfix postfix/mailname string mail.example.com | debconf-set-
selections  
  
RUN apt-get update ; apt-get install -q -y language-pack-en postfix mailutils
rsyslog supervisor ; apt-get clean  
  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN update-locale LANG=en_US.UTF-8  
  
RUN postconf -e "myorigin = \$myhostname"  
RUN postconf -e "message_size_limit = 52400000"  
RUN postconf -e "mynetworks_style = subnet"  
RUN postconf -X "mynetworks"  
  
ADD start_postfix.sh /usr/local/bin/start_postfix.sh  
RUN chmod +x /usr/local/bin/start_postfix.sh  
  
ADD launcher.sh /launcher.sh  
RUN chmod +x /launcher.sh  
  
expose 25  
cmd /launcher.sh

