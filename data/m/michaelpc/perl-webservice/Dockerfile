FROM michaelpc/perl-base:latest  
  
RUN mkdir /tmp/installation  
  
WORKDIR /tmp/installation  
  
RUN apt-get install -y nginx  
  
RUN curl http://uwsgi.it/install | bash -s psgi $PWD/uwsgi; chmod +vx
$PWD/uwsgi; cp -v $PWD/uwsgi /usr/bin  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -; apt-get install
nodejs npm; npm install -g localtunnel  
  
#RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:certbot/certbot;
apt-get update; apt-get install -y python python-dev python-pip python-
certbot-nginx  
RUN cpanm --notest Dancer2  
RUN cpanm --notest YAML  
RUN cpanm --notest Template  
RUN cpanm --notest Plack  
RUN cpanm --notest Starman  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3000  
EXPOSE 5000  
RUN rm -fr /tmp/installation  
  
WORKDIR /web  
  
VOLUME /web  

