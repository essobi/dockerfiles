FROM centos:latest  
MAINTAINER thedancannon <dan@mattymoose.com>  
  
  
# Set correct environment variables  
ENV HOME /root  
ENV TZ America/New_York  
  
# Set timezone  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN yum -y install epel-release # Install EPEL repo  
RUN yum -y install http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el7.rf.x86_64.rpm  
  
# Install Dependancies  
RUN yum -y install scl-utils ca-certificates wget unrar unzip git gcc make  
  
#Install Python 2.7.10  
RUN wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz  
RUN tar xzf Python-2.7.10.tgz  
RUN ./Python-2.7.10/configure  
RUN ls ./Python-2.7.10/  
RUN cd ./Python-2.7.10/  
RUN make altinstall  
  
EXPOSE 8081  
# SickRage Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# TV directory  
VOLUME /tv  
  
#run sickrage  
ADD start_sickrage.sh /opt/start_sickrage.sh  
RUN chmod +x /opt/start_sickrage.sh  
  
CMD /opt/start_sickrage.sh

