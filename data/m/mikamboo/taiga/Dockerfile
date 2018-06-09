FROM ubuntu:16.04  
MAINTAINER mike@mikangali.com  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential binutils-doc autoconf flex bison libjpeg-dev libfreetype6-dev
zlib1g-dev \  
libzmq3-dev libgdbm-dev libncurses5-dev automake libtool libffi-dev curl git
tmux gettext sudo \  
python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper
libxml2-dev \  
libxslt-dev rabbitmq-server redis-server nodejs nodejs-legacy npm circus nginx
postgresql-9.5 \  
postgresql-contrib-9.5 postgresql-doc-9.5 postgresql-server-dev-9.5 supervisor  
  
# Create taiga user  
RUN useradd -ms /bin/bash taiga  
  
ADD ./install /home/taiga/  
  
WORKDIR /home/taiga  
  
RUN chmod +x bootstarp.sh && chmod +x install.sh && ./install.sh  
  
VOLUME ["/home/taiga", "/var/lib/postgresql", "/etc/postgresql"]  
  
CMD ["/home/taiga/bootstarp.sh"]  
  
EXPOSE 80

