FROM ubuntu:14.04  
  
MAINTAINER Matt Titmus <matthew.titmus@gmail.com>  
  
ENV MUD_VERSION 3.8.6  
ENV MUD_DOWNLOAD_URL http://dead-souls.net/code/ds${MUD_VERSION}.zip  
ENV MUD_HOME /home/mud  
  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends bison gcc libc6 libc6-dev make
telnet wget unzip \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd -ms /bin/bash mud  
  
USER mud  
  
WORKDIR ${MUD_HOME}  
  
# Get the MUD source from the Dead Souls site  
RUN wget ${MUD_DOWNLOAD_URL} \  
&& unzip ds${MUD_VERSION}.zip \  
&& rm ds${MUD_VERSION}.zip \  
&& mv ds${MUD_VERSION} ds \  
&& rm -Rf ds/win32 \  
&& rm ds/runmud.bat  
  
# Tar up the /lib directory. If the lib directory is found to be empty (if it
is volumed, for example),  
# then it will be filled from here.  
  
WORKDIR ${MUD_HOME}/ds/lib  
  
RUN tar cfz lib.tgz * \  
&& mv lib.tgz ..  
# Build the MUD driver from source (TODO: I'm pretty sure we can remove this
afterwards)  
  
WORKDIR ${MUD_HOME}/ds/fluffos-2.23-ds03  
  
RUN ./configure \  
&& make install  
  
EXPOSE 6666  
  
WORKDIR ${MUD_HOME}/ds  
  
# Lib directory is a volume, so configuration and build history can be
persisted and survive restarts  
VOLUME ${MUD_HOME}/ds/lib  
# On startup, we check to see if the lib directory is empty (i.e., if it's
been volumed  
# over). If so, we refill it from the tar file.  
CMD if [ $(/bin/ls -A lib | wc -l) -eq 0 ]; then mv lib.tgz lib; cd lib; tar
xfz lib.tgz; rm lib.tgz; cd ..; fi \  
&& ./bin/driver /home/mud/ds/bin/mudos.cfg  
  

