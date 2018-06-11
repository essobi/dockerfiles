FROM clue/ttrss  
MAINTAINER Daniel Miller <watermelonpizza@melonstudios.net>  
  
RUN echo "deb http://au.archive.ubuntu.com/ubuntu/ xenial main" >
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y wget unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/levito/tt-rss-feedly-theme/archive/master.zip && \  
unzip master.zip  
  
RUN cp tt-rss-feedly-theme-master/feedly.css themes && \  
cp -r tt-rss-feedly-theme-master/feedly themes  
  
RUN rm master.zip && \  
rm -r tt-rss-feedly-theme-master  

