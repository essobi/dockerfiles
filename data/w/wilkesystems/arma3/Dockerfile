FROM wilkesystems/steamcmd:stretch  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
ADD arma3.tar.xz /  
  
RUN apt-get update; \  
apt-get install -y bzip2 cron curl exim4-daemon-light p7zip rsyslog supervisor
unzip wget xz-utils; \  
groupadd -g 999 steam; useradd -d /home/steam -g 999 -m -r -u 999 steam; \  
mkdir -p -m 770 /usr/games/arma3; chown steam:steam /usr/games/arma3; \  
su -s /bin/bash -l steam -c 'steamcmd +quit'; \  
rm -rf /root/.steam /var/lib/apt/lists/*;  
  
COPY docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
  
EXPOSE 2301-2305/udp 9001/tcp  
  
WORKDIR /usr/games/arma3  
  
CMD ["supervisor"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]

