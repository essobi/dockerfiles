FROM debian:latest  
  
MAINTAINER Dave Dobson <ddobson@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update -y -q && \  
apt-get install -y -q --no-install-recommends \  
iptables \  
exim4 \  
bsd-mailx \  
whois \  
python \  
python3 \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/src && \  
/usr/bin/git -c http.sslVerify=false clone -b debian-0.10
https://github.com/fail2ban/fail2ban.git && \  
cd fail2ban && \  
/usr/bin/python3 setup.py install  
  
COPY filter.d/ /etc/fail2ban/filter.d/  
COPY action.d/ /etc/fail2ban/action.d/  
COPY jail.conf /etc/fail2ban/jail.local  
  
RUN mkdir -p /var/run/fail2ban  
RUN rm -f /etc/fail2ban/jail.d/defaults-debian.conf  
  
RUN sed -i -e 's/logtarget = \/var\/log\/fail2ban.log/logtarget = STDOUT/g'
/etc/fail2ban/fail2ban.conf  
  
CMD ["-f", "start"]  
ENTRYPOINT ["/usr/local/bin/fail2ban-server"]  

