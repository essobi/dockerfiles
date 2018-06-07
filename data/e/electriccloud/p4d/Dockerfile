FROM ubuntu  
MAINTAINER Nikhil Vaze  
  
  
ENV P4JOURNAL /var/log/perforce/journal  
ENV P4LOG /var/log/perforce/p4err  
ENV P4PORT 1666  
ENV P4ROOT /perforce_depot  
ENV P4USER testuser  
ENV P4PASSWD testuser  
ENV P4CLIENT perforce-test  
ENV HOME /home/perforce  
  
# Update apt sources  
RUN apt-get update  
  
# create Perforce user & group  
RUN addgroup p4admin  
RUN useradd -m -g p4admin perforce  
  
# Install perforce server  
ADD http://filehost.perforce.com/perforce/r14.1/bin.linux26x86_64/p4d
/usr/local/sbin/  
  
# Install perforce client  
ADD http://filehost.perforce.com/perforce/r14.1/bin.linux26x86_64/p4
/usr/local/bin/  
  
RUN chmod +x /usr/local/sbin/p4d /usr/local/bin/p4  
  
RUN mkdir $P4ROOT  
RUN chown perforce:p4admin $P4ROOT  
RUN mkdir /var/log/perforce  
  
RUN chown perforce:p4admin /var/log/perforce  
  
# Populate test workspace and perforce database  
RUN apt-get install wget -y  
RUN wget -O /tmp/sampledepot.tar.gz
http://ftp.perforce.com/perforce/tools/sampledepot.tar.gz  
  
RUN tar xfz /tmp/sampledepot.tar.gz -C /tmp; rm -rf $P4ROOT/db.*; cp -Rf
/tmp/PerforceSample/* $P4ROOT  
  
RUN mkdir -p $HOME/Perforce; chown -R perforce:p4admin $HOME  
  
RUN chown -R perforce:p4admin $P4ROOT  
  
USER perforce  
RUN p4d -r $P4ROOT -jr $P4ROOT/checkpoint;  
  
ENTRYPOINT p4d  
  
# Expose port  
EXPOSE 1666  

