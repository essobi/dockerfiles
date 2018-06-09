FROM ubuntu:16.04  
MAINTAINER Mykhaylo Kolesnik "https://github.com/tenequm"  
# Installing basic important tools.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python-software-properties \  
software-properties-common \  
rsyslog systemd systemd-cron sudo openssh-server \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
RUN sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf  
  
# Configuring OpenSSH server.  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

