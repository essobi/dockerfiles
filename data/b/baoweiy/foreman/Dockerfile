FROM ubuntu:trusty  
  
MAINTAINER "bw.y" <baowei.y@gmail.com>  
  
ENV LANG "en_US.UTF-8"  
ENV LANGUAGE "en_US:en"  
RUN mv /etc/localtime /etc/localtime.bak && \  
ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
mv /sbin/initctl /sbin/oldinitctl && \  
echo -e '#!/bin/bash\nif [[ $1 == "--version" ]];then\n echo "initctl (upstart
1.12.1)"\nfi\n/sbin/oldinitctl "$@"' > /sbin/initctl && \  
chmod 755 /sbin/initctl  
  
RUN apt-get -y install curl wget ca-certificates && apt-get update  
  
RUN echo "deb http://deb.theforeman.org/ trusty nightly" >
/etc/apt/sources.list.d/foreman.list && \  
echo "deb http://deb.theforeman.org/ plugins nightly" >>
/etc/apt/sources.list.d/foreman.list  
  
RUN curl http://deb.theforeman.org/pubkey.gpg | apt-key add - && \  
wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb -P /tmp/ && \  
dpkg -i /tmp/puppetlabs-release-trusty.deb && rm -f /tmp/puppetlabs-release-
trusty.deb && apt-get update  
  
RUN apt-get install -y foreman-postgresql foreman mcollective mcollective-
client mcollective-common mcollective-puppet-agent mcollective-puppet-client
mcollective-puppet-common foreman-cli ruby-foreman-setup ruby-hammer-cli-
foreman postgresql-9.3 postgresql-client-9.3 postgresql-client-common
postgresql-common puppetmaster-common syslinux apache2 libapache2-mod-
passenger tftpd-hpa foreman-installer puppetmaster  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8140  
EXPOSE 8443  
ENTRYPOINT ["/entrypoint.sh"]  

