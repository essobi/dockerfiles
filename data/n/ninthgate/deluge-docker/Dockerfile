FROM debian:jessie  
  
#add to start script or compose to set login:pass  
#ENV LOGIN  
#ENV PASSWORD  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV DELUGE_HOME /home/deluge  
ENV DELUGE_CONFIG_DIR ${DELUGE_HOME}/config  
ENV DELUGE_DATA_DIR ${DELUGE_HOME}/data  
  
# Install components  
RUN echo 'deb http://ppa.launchpad.net/deluge-team/ppa/ubuntu trusty main' >>
/etc/apt/sources.list  
RUN KEY=C5E6A5ED249AD24C && gpg --keyserver pgpkeys.mit.edu --recv-key $KEY &&
gpg -a --export $KEY | apt-key add -  
  
RUN apt-get update  
RUN apt-get --no-install-recommends -t jessie -qyy install sudo runit unzip
wget zip  
RUN apt-get --no-install-recommends -t trusty -qyy install deluged python-
libtorrent  
  
#for debug purpose  
RUN apt-get -qyy -t jessie install nano lsof  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd -m -s /bin/nologin deluge  
RUN mkdir -p ${DELUGE_DATA_DIR} ${DELUGE_CONFIG_DIR}
${DELUGE_DATA_DIR}/autoadd ${DELUGE_HOME}/tmp  
  
#copy predefined config files  
ADD core.conf ${DELUGE_HOME}/tmp  
# Expose ports  
EXPOSE 11961  
EXPOSE 1113  
VOLUME ${DELUGE_CONFIG_DIR}  
VOLUME ${DELUGE_DATA_DIR}  
  
ADD entrypoint.sh /home/deluge  
RUN chmod +x /home/deluge/entrypoint.sh  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/home/deluge/entrypoint.sh"]  

