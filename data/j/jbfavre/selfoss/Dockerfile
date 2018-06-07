FROM debian:latest  
MAINTAINER Jean Baptiste Favre <docker@jbfavre.org>  
  
  
ENV SHELL "/bin/bash"  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM 1  
  
ADD scripts/debian_cleaner.sh /tmp/  
  
RUN /usr/bin/apt-get update -yqq \  
&& /usr/bin/apt-get upgrade --no-install-recommends -yqq \  
&& /usr/bin/apt-get install --no-install-recommends -yqq curl ca-certificates
\  
php5-cli php5-apcu php5-curl php5-gd php5-sqlite \  
&& /usr/bin/chsh -s /bin/bash root \  
&& /bin/rm /bin/sh && ln -s /bin/bash /bin/sh \  
&& /usr/sbin/groupadd -r selfoss \  
&& /usr/sbin/useradd -r -m -s /bin/bash -g selfoss selfoss \  
&& /usr/bin/curl -L -o /tmp/selfoss.tar.gz
https://github.com/SSilence/selfoss/archive/2.15.tar.gz \  
&& /bin/su \- selfoss -c '/bin/tar xzf /tmp/selfoss.tar.gz -C /home/selfoss
--strip-components=1' \  
&& /bin/rm -f /tmp/selfoss.tar.gz \  
&& /bin/rm -f /home/selfoss/selfoss*.zip \  
&& /bin/mkdir /var/lib/selfoss \  
&& /bin/chown -R selfoss: /var/lib/selfoss \  
&& /bin/bash /tmp/debian_cleaner.sh  
  
VOLUME /var/lib/selfoss  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
ADD ./docker-entrypoint.sh /usr/local/bin/  
ADD ./run.php /home/selfoss/  
  
EXPOSE 8080  

