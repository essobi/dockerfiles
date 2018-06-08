FROM ubuntu:14.04  
MAINTAINER Samuel Warkentin <s.warkentin@mittwald.de>  
  
# no need for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# set timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# ...put your own build instructions here...  
RUN apt-get -qq update  
RUN apt-get -y install spamassassin imapfilter python razor pyzor unp python-
pip python-setuptools wget unzip rsyslog git  
RUN pip install --upgrade pip && pip install setuptools docopt==0.6.2  
RUN cd root && mkdir .spamassassin  
RUN cd /tmp && git clone https://github.com/isbg/isbg.git && cp isbg/isbg.py
/bin/ && chmod +x /bin/isbg.py && rm -rf /tmp/isbg  
ADD user_prefs /root/.spamassassin/user_prefs  
ADD default_spamassassin /etc/default/spamassassin  
ADD start.sh /start.sh  
ADD cron_spamassassin /etc/cron.daily/spamassassin  
  
# Clean up APT when done.  
RUN apt-get autoremove --purge  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN touch /INIT  
  
CMD cron && bash /start.sh  

