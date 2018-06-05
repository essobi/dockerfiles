FROM krallin/ubuntu-tini:16.04  
MAINTAINER Seti <seti@setadesign.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV UBUNTU_NAME xenial  
  
COPY assets/init.sh /  
RUN apt-get update && apt-get install -y wget opendkim \  
opendkim-tools openssl rsyslog &&\  
wget -O- https://rspamd.com/apt-stable/gpg.key | apt-key add - && \  
echo "deb http://rspamd.com/apt-stable/ $UBUNTU_NAME main" >
/etc/apt/sources.list.d/rspamd.list && \  
echo "deb-src http://rspamd.com/apt-stable/ $UBUNTU_NAME main" >>
/etc/apt/sources.list.d/rspamd.list && \  
apt-get update && \  
apt-get --no-install-recommends install -y rmilter && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod 0755 /*.sh  
  
COPY assets/conf/rmilter.conf /etc/rmilter.conf  
COPY assets/rsyslog.conf /etc/rsyslog.conf  
  
EXPOSE 9900  
VOLUME ["/dkimkeys"]  
CMD /init.sh; rmilter -c /etc/rmilter.conf; rsyslogd -n  

