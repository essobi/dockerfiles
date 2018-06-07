FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV PERL_MM_USE_DEFAULT 1  
ENV TZ=Europe/Berlin  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y cron libdbd-sqlite3-perl python-pip unzip wget ssh-
client libnet-amazon-ec2-perl rsync libdata-dumper-simple-perl lame vorbis-
tools clamav ssmtp mailutils git zip  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN pip install --upgrade pip  
RUN pip install --upgrade google-api-python-client progressbar2  
  
RUN mkdir /install  
RUN cd /install && git clone https://github.com/tokland/youtube-upload.git &&
cd youtube-upload && python setup.py install  
RUN rm -rf /install  
  
RUN perl -MCPAN -e 'install WebService::Amazon::Route53'  
  
RUN mkdir /data  
RUN mkdir /data/cronjobs  
RUN rm -rf /etc/cron.d && ln -s /data/cronjobs /etc/cron.d  
RUN rm /etc/ssmtp/ssmtp.conf && touch /data/ssmtp.conf && ln -s
/data/ssmtp.conf /etc/ssmtp/ssmtp.conf  
RUN touch /data/id_rsa && touch /data/id_rsa.pub && mkdir /root/.ssh && ln -s
/data/id_rsa /root/.ssh/id_rsa && ln -s /data/id_rsa.pub /root/.ssh/id_rsa.pub
&& touch /data/known_hosts && ln -s /data/known_hosts /root/.ssh/known_hosts  
  
ADD start.sh /start.sh  
RUN chmod 700 /start.sh  
  
CMD ["/start.sh"]  

