FROM debian:jessie  
  
  
## Prereq  
ADD sources.list /etc/apt/  
ADD preferences /etc/apt/  
  
RUN apt-get --quiet update && apt-get --quiet install --yes --no-install-
recommends \  
make build-essential python-jinja2 python-pkg-resources ninja-build bzip2
rsync openjdk-8-jdk-headless zip vim ssh git-core autoconf automake \  
&& apt-get clean  
  
## DS specific  
ENV LEGATO_ROOT /legato  
ENV PATH $LEGATO_ROOT/bin:$PATH  
ENV LEGATO_LOCALHOST_LIB_PATH $LEGATO_ROOT/build/localhost/bin/lib/  
ENV TOOLCHAIN_PROFILES /opt/swi/profiles.d  
  
## Legato env  
ADD legatoenv /legatoenv  
RUN echo "source /legatoenv" >> /etc/bash.bashrc  
ENV BASH_ENV /legatoenv  
  
WORKDIR /  
  

