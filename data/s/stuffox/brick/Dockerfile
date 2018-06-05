FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
build-essential curl git \  
libssl-dev  
  
RUN curl -sL http://cpanmin.us | perl - App::cpanminus \  
&& cpanm --notest --mirror http://cpan.org \  
Module::Build \  
LWP::Protocol::https \  
https://github.com/stuffox/stuffox-brick.git \  
&& mkdir -p /opt/brick  
  
VOLUME /opt/brick  
  
EXPOSE 8080  
ENTRYPOINT /usr/local/bin/brick.pl serve --path /opt/brick --port 8080  

