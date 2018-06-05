FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SBFSPOT_HOME /home/sbfspot  
ENV SMADATA /var/smadata  
ENV SBFSPOTDIR /opt/sbfspot  
  
ARG user=sbfspot  
ARG group=sbfspot  
ARG uid=2000  
ARG gid=2000  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$SBFSPOT_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bluetooth \  
libbluetooth-dev \  
libboost-all-dev \  
sqlite3 \  
libsqlite3-dev \  
libcurl3-dev \  
default-libmysqlclient-dev \  
make \  
g++ \  
mercurial \  
ca-certificates \  
patch \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-ca-certificates  
  
# Make SBFspot and move installation to SBFSPOTDIR. SBFspot by default
installs to /usr/local/bin/sbfspot.3  
WORKDIR $SBFSPOT_HOME/sbfspot.3  
COPY V332.patch $SBFSPOT_HOME/sbfspot.3  
COPY SBFspot_*.tar.gz $SBFSPOT_HOME/sbfspot.3  
# wget https://sbfspot.codeplex.com/downloads/get/1575948  
RUN tar -xvf SBFspot_*.tar.gz \  
&& grep -qe 'VERSION "3.3.1"' SBFspot/SBFspot.cpp \  
&& cd SBFspot/ \  
&& patch -p 1 < ../V332.patch  
  
# Compile SBFspot  
WORKDIR $SBFSPOT_HOME/sbfspot.3/SBFspot  
RUN make install_mysql  
  
# Compile SBFspotUploadDaemon  
WORKDIR $SBFSPOT_HOME/sbfspot.3/SBFspotUploadDaemon  
RUN make install_mysql  
  
WORKDIR $SBFSPOT_HOME  
  
# Deinstall compiler since we no longer need it  
RUN apt-get -y purge \  
g++ \  
make \  
mercurial \  
patch \  
&& apt-get -y autoremove \  
&& apt-get -y autoclean  
  
RUN mv /usr/local/bin/sbfspot.3 $SBFSPOTDIR \  
&& cp $SBFSPOT_HOME/sbfspot.3/SBFspot/CreateSQLiteDB.sql $SBFSPOTDIR \  
&& cp $SBFSPOT_HOME/sbfspot.3/SBFspot/CreateMySQL*.sql $SBFSPOTDIR \  
&& rm -rf $SBFSPOT_HOME/sbfspot.3  
  
COPY start.sh $SBFSPOTDIR/  
RUN chmod +x $SBFSPOTDIR/start.sh  
  
# Setup data directory  
RUN mkdir $SMADATA && chown -R ${user}:${group} $SMADATA  
  
VOLUME ["/var/smadata", "/opt/sbfspot"]  
  
USER ${user}  
  
CMD [ "/opt/sbfspot/start.sh" ]  

