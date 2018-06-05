FROM debian:jessie  
  
ENV BORG_VERSION=1.0.11 \  
LANG=C.UTF-8  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --force-yes apt-transport-https ca-certificates curl\  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& sed -i "s/httpredir.debian.org/`curl -s -D -
http://httpredir.debian.org/demo/debian/ | awk '/^Link:/ { print $2 }' | sed
-e 's@<http://\\(.*\\)/debian/>;@\1@g'`/" /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
docker-engine=1.8.3-0~jessie \  
openssh-server \  
python3-pip \  
build-essential \  
libssl-dev \  
libssl1.0.0 \  
liblz4-dev \  
liblz4-1 \  
libacl1-dev \  
libacl1 \  
&& rm -f /etc/ssh/ssh_host_* \  
&& pip3 install borgbackup==$BORG_VERSION \  
&& apt-get remove -y --purge build-essential libssl-dev liblz4-dev libacl1-dev
\  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/* \  
&& adduser --uid 500 \--disabled-password --gecos "Borg Backup" \--quiet borg
\  
&& mkdir /var/run/sshd \  
&& mkdir /home/borg/.ssh \  
&& chmod 700 /home/borg/.ssh \  
&& chown borg:borg /home/borg/.ssh  
COPY cron /usr/local/bin/  
COPY authorized_keys.sample /home/borg/authorized_keys.sample  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

