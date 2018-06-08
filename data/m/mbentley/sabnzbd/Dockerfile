FROM debian:sid  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN (sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list &&\  
apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates locales
sabnzbdplus &&\  
echo 'LANG="en_US.UTF-8"' >> /etc/default/locale &&\  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen &&\  
rm -rf /var/lib/apt/lists/*)  
  
RUN (ln -sf /usr/share/zoneinfo/US/Eastern /etc/localtime &&\  
groupadd -g 501 sabnzbd &&\  
useradd -u 501 -g 501 -d /etc/sabnzbd sabnzbd &&\  
mkdir /etc/sabnzbd &&\  
chown -R sabnzbd:sabnzbd /etc/sabnzbd)  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
USER sabnzbd  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/sabnzbdplus"]  
CMD ["--config-file","/etc/sabnzbd","--browser","0","--console","--
server",":8080"]  

