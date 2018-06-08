FROM ubuntu:14.04  
MAINTAINER oloc  
# Update Ubuntu  
RUN apt-get -y update && apt-get -y upgrade  
# Install curl and wget  
RUN apt-get -y install curl wget  
# Install puppet stuff  
RUN apt-get -y install puppet librarian-puppet  
RUN puppet module install puppetlabs-stdlib  
RUN puppet module install puppetlabs-apt  
RUN puppet module install deric-mesos  
  
ADD site.pp /root/site.pp  
RUN chmod +x /root/site.pp  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
CMD ["/root/run.sh"]

