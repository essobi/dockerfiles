FROM debian:jessie  
  
MAINTAINER Raphael Bicker  
  
ENV MYSQL_ICINGA_DB icinga2  
ENV MYSQL_ICINGA_USER icinga2  
ENV MYSQL_ICINGA_PASSWORD icinga2  
  
ENV ROOT_PASSWORD root  
ENV NOTVISIBLE "in users profile"  
ENV API_USER api  
ENV API_PASSWORD api  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update \  
&& apt-get -qqy upgrade \  
&& apt-get install -y wget vim mysql-client ssmtp  
  
RUN wget --quiet -O - https://packages.icinga.org/icinga.key | apt-key add -  
  
RUN echo "deb http://packages.icinga.org/debian icinga-jessie main" >>
/etc/apt/sources.list  
  
RUN apt-get update -q \  
&& apt-get install -y icinga2 icinga2-ido-mysql openssh-server  
  
RUN mkdir /var/run/sshd  
RUN echo "root:${ROOT_PASSWORD}" | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ADD content/ /  
  
RUN chmod +x /run.sh  
  
VOLUME ["/etc/icinga2", "/var/lib/icinga2", "/var/log/icinga2", "/etc/ssmtp"]  
  
EXPOSE 5665 22  
CMD ["/run.sh"]

