FROM ubuntu:trusty  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
### ports  
# puppet (via apache)  
EXPOSE 8140  
# foreman-proxy  
EXPOSE 8443  
# foreman (via apache)  
EXPOSE 443  
EXPOSE 80  
ENV DEBIAN_FRONTEND noninteractive  
  
### install prereqs and other userful bits  
RUN apt-get -y update && \  
apt-get -y install curl \  
wget \  
vim \  
git  
  
### set up puppet repos  
WORKDIR /tmp  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb  
RUN dpkg -i puppetlabs-release-trusty.deb  
  
### install foreman installer  
RUN echo "deb http://deb.theforeman.org/ trusty 1.6" >
/etc/apt/sources.list.d/foreman.list  
RUN echo "deb http://deb.theforeman.org/ plugins 1.6" >>
/etc/apt/sources.list.d/foreman.list  
RUN wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add -  
RUN apt-get -y update && apt-get -y install foreman-installer  
  
### install supervisord  
RUN apt-get -y install python-pip  
RUN pip install supervisor  
  
### add supervisor configs  
ADD resources/etc/supervisord.conf /etc/supervisord.conf  
ADD resources/etc/supervisord.d /etc/supervisord.d  
  
### add run scripts  
ADD resources/start.sh /start.sh  
ADD resources/start_postgresql.sh /start_postgresql.sh  
ADD resources/start_foreman-proxy.sh /start_foreman-proxy.sh  
  
### just in case  
RUN chown -R root:root /etc/supervisord*  
RUN mkdir -p /var/log/supervisord  
RUN chmod +x /start*.sh  
  
ENTRYPOINT /start.sh  

