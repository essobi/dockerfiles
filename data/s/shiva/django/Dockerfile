FROM ubuntu:12.10  
MAINTAINER Shavrin Ivan <shavrin.ivan@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
RUN apt-get -qq update  
  
# Install libraries for building psycopg2, PIL and different requirements from
vcs repositories  
  
RUN apt-get -y install postgresql-server-dev-9.1 postgresql-client-9.1 python-
dev  
RUN apt-get -y install --no-install-recommends python-pip git-core mercurial  
RUN apt-get -y install --no-install-recommends libjpeg-dev libfreetype6-dev
zlib1g-dev  
  
# Link libraries for PIL build  
  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/

