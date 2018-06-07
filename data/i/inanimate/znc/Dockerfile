FROM ubuntu:vivid  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -yq --force-yes znc znc-dev znc-dbg znc-dev znc-perl znc-
python znc-tcl make git && \  
apt-get install -yq --force-yes libotr5-dev && \  
apt-get autoremove -yq && apt-get clean  
  
  
# run ZNC as an unprivileged user  
RUN useradd znc  
  
ADD run /znc-run  
RUN chmod +x /znc-run  
  
CMD ["/znc-run"]  
  

