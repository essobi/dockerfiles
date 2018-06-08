FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install logentries daemon  
RUN echo 'deb http://rep.logentries.com/ jessie main' >
/etc/apt/sources.list.d/logentries.list && \  
gpg --keyserver pgp.mit.edu --recv-keys C43C79AD && \  
gpg -a --export C43C79AD | apt-key add - && \  
apt-get update -qq && \  
apt-get install -y python-setuptools python-setproctitle logentries
logentries-daemon && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ADD docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/le", "monitor"]  

