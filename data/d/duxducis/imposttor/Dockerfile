FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_4.x | bash  
  
# Add non-free to access unrar  
RUN echo 'deb http://httpredir.debian.org/debian jessie non-free' >>
/etc/apt/sources.list  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
nodejs \  
build-essential \  
libkrb5-dev \  
ruby \  
curl \  
netcat \  
openvpn \  
unzip \  
iptables \  
dnsutils \  
ssh \  
cron \  
wget \  
rsync \  
unrar  
  
RUN gem install tiller  
  
# Create root directories  
RUN mkdir /openvpn && mkdir /socks  
  
# Set nobody id and gid to match unraid  
RUN usermod -u 99 nobody && usermod -g 100 nobody  
  
# Set the entry point  
ENTRYPOINT ["/init"]  
  
# Expose the two socks ports and the webapp port  
EXPOSE 1080 1081 5000  
# Setup sshd  
RUN mkdir /var/run/sshd && \  
sed -i 's/#AuthorizedKeysFile %h\/.ssh\/authorized_keys/AuthorizedKeysFile
~\/.ssh\/authorized_keys/' /etc/ssh/sshd_config && \  
sed -i 's/#ListenAddress 0.0.0.0/ListenAddress 127.0.0.1/'
/etc/ssh/sshd_config && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Allow password login  
#RUN echo 'root:password' | chpasswd  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# Install services  
COPY services /etc/services.d  
  
# Install init.sh as init script  
COPY init.sh /etc/cont-init.d/  
  
# Copy tiller configuration  
COPY data /etc/tiller  
  
#RUN touch /etc/services.d/openvpn/down  
# Setup monitoring via cron  
RUN printf '*/2 * * * * /usr/bin/monitor\n' | crontab  
  
# Don't start vpn-socks, seedbox-socks or post-process (will be started when
VPN connects)  
RUN touch /etc/services.d/vpn-socks/down && \  
touch /etc/services.d/seedbox-socks/down && \  
touch /etc/services.d/post-process/down  
  
COPY app /app  
  
# Download and extract s6 init  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.10.0.3/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
# Download and install certificates from PIA to /openvpn  
ADD https://www.privateinternetaccess.com/openvpn/openvpn.zip /tmp/  
RUN unzip -d /tmp /tmp/openvpn.zip && mv /tmp/ca.rsa.2048.crt /openvpn/ && mv
/tmp/crl.rsa.2048.pem /openvpn/ && rm -rf /tmp/*  

