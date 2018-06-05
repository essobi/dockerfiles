FROM debian:8.5  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
RUN apt-get install libboost-iostreams-dev -y  
RUN apt-get install zlib1g-dev -y  
RUN apt-get install make -y  
RUN apt-get install wget -y  
RUN apt-get install perl -y  
RUN apt-get install g++ -y  
RUN echo "mysql-server mysql-server/root_password password toto" | debconf-
set-selections  
RUN echo "mysql-server mysql-server/root_password_again password toto" |
debconf-set-selections  
RUN apt-get install mysql-server -y  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu vivid main universe' >>
/etc/apt/sources.list  
RUN apt-get install bamtools libbamtools-dev -y  
RUN apt-get install -y cpanminus  
RUN cpanm File::Spec::Functions File::Basename DBI  
RUN cd /tmp &&\  
wget http://bioinf.uni-greifswald.de/augustus/binaries/augustus-3.2.2.tar.gz
&&\  
tar xvzf augustus-3.2.2.tar.gz &&\  
cd augustus-3.2.2 &&\  
make &&\  
make install  
ENV AUGUSTUS_CONFIG_PATH /opt/augustus-3.2.2/config/  
RUN chmod -R 777 /opt/augustus-3.2.2/config/species  

