FROM jahroots/java  
MAINTAINER Jahroots "jahroots@gmail.com"  
ENV CRUCIBLE_VERSION 3.7.0  
### Install and configure packages  
RUN apt-get update && apt-get clean  
RUN apt-get install -y openssh-server supervisor unzip wget  
RUN mkdir -p /var/run/sshd  
RUN chmod 755 /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
### Download and unzip Crucible  
RUN wget --no-check-certificate -P /opt
http://www.atlassian.com/software/crucible/downloads/binary/crucible-${CRUCIBLE_VERSION}.zip  
RUN cd /opt && unzip crucible-${CRUCIBLE_VERSION}.zip && rm
crucible-${CRUCIBLE_VERSION}.zip && mv fecru-${CRUCIBLE_VERSION} fecru  
  
### Configure ssh  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
### Clean  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
RUN apt-get -y autoremove  
  
### Add supervisord.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
### Share /opt  
VOLUME ["/opt/"]  
  
### Expose port  
EXPOSE 22 8060  
###  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

