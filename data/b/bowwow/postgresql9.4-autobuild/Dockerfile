FROM ubuntu:14.04  
MAINTAINER bowwow "bowwow@bowwow.com"  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
RUN sudo apt-get install -y software-properties-common  
RUN sudo add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/
trusty-pgdg main"  
  
RUN sudo apt-get install -y apt-transport-https wget  
RUN wget --quiet -O - https://postgresql.org/media/keys/ACCC4CF8.asc | sudo
apt-key add -  
RUN sudo apt-get update  
RUN sudo apt-get install -y -q postgresql-9.4 postgresql-contrib-9.4
postgresql-9.4-postgis-2.1 libpq-dev  
  
# /etc/ssl/private can't be accessed from within container for some reason  
# (@andrewgodwin says it's something AUFS related)  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
ADD postgresql.conf /etc/postgresql/9.4/main/postgresql.conf  
ADD pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
RUN chown postgres:postgres /etc/postgresql/9.4/main/*.conf  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
VOLUME ["/var/lib/postgresql"]  
EXPOSE 5432  
CMD ["/usr/local/bin/run"]  

