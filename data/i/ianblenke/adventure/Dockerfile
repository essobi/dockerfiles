FROM centurylink/wetty-cli  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
# Install build dependencies  
RUN apt-get -qqy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential f2c
supervisor python-pip screen procps net-tools bsdutils unzip wget
libgfortran-4.8-dev  
  
RUN chown daemon:daemon /etc/supervisor/conf.d/ /var/run/ /var/log/supervisor/  
  
RUN pip install supervisor-stdout  
  
WORKDIR /adventure  
  
# Download and compile adventure  
RUN wget http://www.ifarchive.org/if-archive/games/source/advsrc.zip && \  
unzip advsrc.zip  
  
ADD Makefile /adventure/Makefile  
  
RUN make -C /adventure compile  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
VOLUME /adventure  
  
EXPOSE 3000  
CMD /run.sh  

