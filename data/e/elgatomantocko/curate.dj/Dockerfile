FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y icecast2 mpd mpc redis-server python-pip python-dev  
  
# Install pip deps  
RUN sudo pip install python-mpd2 flask gunicorn gevent redis awscli  
  
# Bundle app source  
ADD . /src  
  
# Link configuration files  
ADD ./mpd.conf /etc/mpd.conf  
ADD ./icecast.xml /etc/icecast2/icecast.xml  
  
EXPOSE 8000  
EXPOSE 80  
RUN aws s3 cp --recursive s3://curatedj /var/lib/mpd/music  
RUN service mpd stop  
RUN service mpd start  
  
CMD icecast2 -c /etc/icecast2/icecast.xml & ./src/monitor.sh
/var/log/icecast2/playlist.log & python ./src/curatedj.py  

