FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
ntpdate \  
tor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin tor && \  
mkdir /home/tor && \  
chown tor:tor -R /home/tor  
  
ADD ./torrc /etc/tor/torrc  
  
EXPOSE 8080  
USER tor  
  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  

