FROM debian:stable-slim  
MAINTAINER Bob Hartlaub <bhartlaub@grassroots-tech.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup workdir  
RUN mkdir -p /root/work/  
WORKDIR /root/work/  
  
# install git and git-ftp  
# - git-ftp: adds ftp functionality to allow uploading changed files only
(bandwidth/pipeline-minute saver)  
# - more info: https://github.com/git-ftp/git-ftp  
RUN apt-get -y update && apt-get -y install git git-ftp  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  
# turn on/off FTP SSL  
# - uncomment line below to allow insecure ftp requests  
# +RUN git config git-ftp.insecure 1  

