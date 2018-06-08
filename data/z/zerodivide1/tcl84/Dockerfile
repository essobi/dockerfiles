FROM ubuntu  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive to get  
# apt-get working without error output.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update underlying ubuntu image and all necessary packages.  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y tcl8.4 \  
tcllib \  
tcl-thread \  
tcl-tclreadline \  
tcl-tls \  
tcl-trf \  
tcl-udp \  
tcl-vfs \  
tclcurl \  
tclgeoip \  
tclodbc \  
tclxml \  
tdom \  
tcl-tclex \  
tcl-memchan \  
tcl-combat \  
tcl-signal \  
tcl-sugar \  
libpgtcl \  
libsqlite-tcl \  
mysqltcl \  
itcl3 \  
critcl \  
xotcl \  
tclxapian \  
libtcl-chiark-1 \  
jq && \  
apt-get clean  
  
# Arrange for a decent tclreadline prompt in interactive mode  
COPY tclshrc /root/.tclshrc  
  
# Export two volumes, one for tcl code and one for data, just in case.  
VOLUME /opt/tcl  
VOLUME /opt/data  
  
# Make sure code put into the special tcl volume can lazily be filled  
# with packages  
ENV TCLLIBPATH /opt/tcl /opt/tcl/lib  
  
ENV COLUMNS 120  
ENV LINES 35  
  
# And make the core bare tclsh the entrypoint as the default  
ENTRYPOINT ["tclsh8.4"]  

