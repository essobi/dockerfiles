FROM mysql:5.6  
MAINTAINER Martin Schnabel <mcnilz@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
rsync \  
gnupg \  
duply \  
automysqlbackup \  
python-boto \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
  
RUN mkdir /root/.duply  
  
VOLUME /root/.duply  
  
WORKDIR /root/.duply  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD []  

