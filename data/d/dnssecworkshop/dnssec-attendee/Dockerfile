# Image: dnssec-attendee  
# Startup a docker container with sshd and named for attendees  
FROM dnssecworkshop/dnssec-bind  
  
MAINTAINER dape16 "dockerhub@arminpech.de"  
LABEL RELEASE=20171030-2234  
  
# Set timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Install software  
RUN echo "postfix postfix/mailname string dnssec-attendee" | debconf-set-
selections  
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-
set-selections  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y --no-install-recommends mailutils postfix nginx  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Deploy DNSSEC workshop material  
RUN cd /root && git clone https://github.com/dnssec-workshop/dnssec-data && \  
rsync -v -rptgoD --copy-links /root/dnssec-data/dnssec-attendee/ /  
  
RUN chgrp bind /etc/bind/zones && chmod g+w /etc/bind/zones  
  
# Start services using supervisor  
RUN mkdir -p /var/log/supervisor  
  
EXPOSE 22 25 53 80 443 465  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/dnssec-
attendee.conf" ]  
  
# vim: set syntax=docker tabstop=2 expandtab:  

