# Run with:  
# docker run -d -it --name=pure-ftpd \  
# --cap-add=SYS_NICE --cap-add=DAC_READ_SEARCH \  
# -p 21:21 -p 35000-35099:35000-35099 \  
# -v pure-ftpd-vol:/etc/pure-ftpd \  
# -v <my data path>:/srv/ftp \  
# -e PUBLICHOST=yourfqdn.com \  
# -e VUSER=<wanted ftp user name> \  
# -e PUID=<UID of data in my data path volume> \  
# -e PGID=<GID of data in my data path volume> \  
# ynsta/pure-ftpd  
# ENVironnement variables:  
#  
# VUSER = Virtual username used to connect to FTP  
# PUID = User ID of data in the /srv/ftp volume  
# GUID = Group ID of data in the /srv/ftp volume  
# PASSIVEMIN = Minimum passive port in pure-ftpd config  
# PASSIVEMAX = Maximum passive port in pure-ftpd config  
# PUBLICHOST = Your full hostname  
# SSL_SUBJ = SSL SUBJ for key generation  
# TLS_MODE = Enable TLS only mode in Pure-FTPd "2". Change to "1" to also
allow insecure mode.  
# Pasword must be changed with:  
# docker exec -it pure-ftpd pure-pw passwd VUSER -m  
FROM debian:stable-slim  
  
LABEL maintainer="Stany MARCEL <stanypub@gmail.com>"  
LABEL version="0.3"  
LABEL description="Pure-FTPd Debian based image"  
  
  
ENV LANG=C.UTF-8 \  
VUSER=ftp \  
PUID=1000 \  
PGID=1000 \  
PASSIVEMIN=35000 \  
PASSIVEMAX=35099 \  
PUBLICHOST=localhost \  
SSL_SUBJ="/C=CN/ST=STATE/L=CITY/O=ORGANISATION/OU=U/CN=localhost" \  
TLS_MODE=2  
  
# Update and intall required packages  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y --fix-missing pure-ftpd openssl pwgen  
  
COPY run.sh /run.sh  
RUN chmod u+x /run.sh  
  
VOLUME ["/srv/ftp", "/etc/pure-ftpd", "/etc/ssl/private"]  
  
CMD /run.sh  
  
EXPOSE 21 35000-35099  

