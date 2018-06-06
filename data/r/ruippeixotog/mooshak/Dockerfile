FROM ubuntu:12.04  
MAINTAINER Rui Gonçalves <ruippeixotog@gmail.com>  
  
RUN apt-get update  
  
# install prerequisites  
RUN apt-get install -y gcc make tcl apache2 apache2-suexec supervisor  
RUN apt-get install -y lpr time cron host rsync libxml2-utils xsltproc  
  
RUN bash -c '\  
cd /etc/apache2/mods-enabled;\  
ln -s ../mods-available/userdir.conf;\  
ln -s ../mods-available/userdir.load;\  
ln -s ../mods-available/suexec.load;'  
  
ADD apache-userdir.conf /etc/apache2/mods-available/userdir.conf  
RUN mkdir -p /var/run/apache2  
  
# install Mooshak  
ADD https://mooshak.dcc.fc.up.pt/download/mooshak-1.5.2.tgz mooshak-1.5.2.tgz  
RUN tar xzf mooshak-1.5.2.tgz  
RUN cd mooshak-1.5.2 && sed -e 's/proc check_suexec {} {/proc check_suexec {}
{ return;/' < install > install-modded  
RUN cd mooshak-1.5.2 && sh install-modded  
  
EXPOSE 80  
VOLUME /home/mooshak/data  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD /usr/bin/supervisord  

