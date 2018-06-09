FROM arwineap/docker-ubuntu-python3.6  
  
RUN apt-get update  
  
#setup japanese environment  
RUN apt-get install -y language-pack-ja-base language-pack-ja ibus-mozc  
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  
  
#install basic modules  
RUN ln -s python3.6 /usr/bin/python  
RUN apt-get install -y wget vim xvfb cron bzip2  
RUN pip install selenium slacker pandas pyvirtualdisplay  
  
#setup phantomJS  
RUN wget -O /usr/local/bin/phantomjs.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -jxvf /usr/local/bin/phantomjs.tar.bz2 -C /usr/local/bin  
RUN mv /usr/local/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
RUN rm /usr/local/bin/phantomjs.tar.bz2  
RUN rm -rf /usr/local/bin/phantomjs-2.1.1-linux-x86_64  
  
#setup & start cron  
RUN touch /var/log/cron.log  
CMD cron && tail -f /var/log/cron.log  
  
########################################################  
# 1. Run docker with the following option.  
# -v /etc/cron.d:/etc/cron.d  
# 2. Better write redirect to logfile in your cronfiles.  
# * * * * * root COMMAND >> /var/log/cron.log  
  

