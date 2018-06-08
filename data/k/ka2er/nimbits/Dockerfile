# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage  
  
MAINTAINER Person Sebastien <personseb@yahoo.fr>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# no need for confirmation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Recommends are as of now still abused in many packages  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/no-recommends  
RUN echo "APT::Get::Assume-Yes "true";" > /etc/apt/apt.conf.d/always-yes  
  
# ...put your own build instructions here...  
RUN apt-get -qq update  
RUN apt-get -y install wget  
RUN echo "deb http://nimbits.com/debian wheezy main" >> /etc/apt/sources.list  
RUN wget -q -O - http://nimbits.com/debian/nimbits.key | apt-key add -  
RUN add-apt-repository ppa:webupd8team/java  
  
RUN apt-get -qq update  
RUN apt-get -q -y install nimbits  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN apt-get install oracle-java7-installer -y  
  
EXPOSE 8080  
#VOLUME [""]  
RUN mkdir /etc/service/nimbits  
ADD nimbits.sh /etc/service/nimbits/run  
  
RUN chmod 600 /etc/crontab  
RUN echo "1 * * * * wget http://localhost:8080/nimbits/cron/idleCron" >>
/etc/crontab && \  
echo "5 * * * * wget http://localhost:8080/nimbits/cron/moveCron" >>
/etc/crontab && \  
echo "10 * * * * wget http://localhost:8080/nimbits/cron/pointCron" >>
/etc/crontab  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

