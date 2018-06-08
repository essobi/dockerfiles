########################################  
# Derived from ubuntu distribution  
########################################  
FROM ubuntu:latest  
MAINTAINER Boris Glavic <bglavic@iit.edu>  
########################################  
# Install packages needed for building  
########################################  
RUN apt-get -y update && apt-get install -y \  
autotools-dev \  
autoconf \  
bison \  
flex \  
git \  
libtool \  
make \  
libreadline6-dev \  
libxml2 \  
libxml2-dev \  
libxslt1-dev \  
sudo \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
########################################  
# Create user (other than root to be able to start postgres  
########################################  
RUN useradd -m perm && echo "perm:perm" | chpasswd && adduser perm sudo  
USER perm  
########################################  
# Create working directories  
########################################  
WORKDIR /home/perm  
########################################  
# Clone Perm github repository  
########################################  
RUN git clone https://github.com/IITDBGroup/perm.git /home/perm/src  
########################################  
# Build Perm  
########################################  
RUN cd /home/perm/src \  
&& ./configure --prefix=/home/perm/install --enable-thread-safety --with-
libxml --with-libxslt CFLAGS='-O0' \  
&& make all \  
&& make install  
########################################  
# Environment  
########################################  
ENV PATH /home/perm/install/bin/:$PATH  
ENV PGDATA /home/perm/datadir  
########################################  
# Expose postmaster port  
########################################  
EXPOSE 5432  
########################################  
# Create Data Directory  
########################################  
RUN cd /home/perm/src && git pull  
RUN ["/home/perm/src/Docker/createExampleCluster.sh","perm"]  
########################################  
# Add datadir as volume to persist across container restarts  
########################################  
VOLUME /home/perm/datadir  
########################################  
# Per default start the gprom command line interface  
########################################  
ENTRYPOINT ["/home/perm/install/bin/postgres"]  
########################################  
# Per default connect to the example SQLite database  
########################################  
CMD ["-D", "/home/perm/datadir"]  

