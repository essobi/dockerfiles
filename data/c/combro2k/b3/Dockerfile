FROM ubuntu-debootstrap:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /data  
VOLUME /data  
  
RUN apt-get update && apt-get dist-upgrade -yq && \  
apt-get install -yq libsqlite3-dev sqlite3 tar git curl nano wget dialog net-
tools build-essential python-mysqldb python python-dev python-distribute
python-pip postgresql-common libpq-dev  
  
WORKDIR /opt  
  
RUN git clone https://github.com/BigBrotherBot/big-brother-bot.git /opt/b3 &&
\  
cd /opt/b3 && git checkout -b release-1.10 origin/release-1.10 && \  
mv /opt/b3/b3/conf /opt/b3/b3/.conf && \  
mv /opt/b3/b3/extplugins /opt/b3/b3/.extplugins && \  
pip install -r /opt/b3/pip-requires.txt  
  
ADD start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
  
ENTRYPOINT ["/opt/start.sh"]  
CMD ["--help"]  

