FROM ubuntu:xenial  
  
# Install Firefox, OpenVPN, and the restricted extras  
RUN apt-get update && apt-get install -y curl firefox openvpn ubuntu-
restricted-extras && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# Install dumb-init  
RUN curl -LO https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb && dpkg -i dumb-init_*.deb && rm dumb-init_*.deb  
  
# Add the Firefox user  
RUN useradd -Um firefox && gpasswd -a firefox audio  
  
# Create a volume for the user's config  
RUN mkdir /data && chown firefox:firefox -R /data  
VOLUME /data  
  
# Add the OpenVPN configs  
ADD openvpn/ /etc/openvpn/  
  
# Add the scripts  
ADD misc/start-ff.sh /openvpn-firefox/start-ff.sh  
ADD misc/stop-ff.sh /openvpn-firefox/stop-ff.sh  
ADD misc/entrypoint.sh /openvpn-firefox/entrypoint.sh  
  
# Add the PulseAudio config  
ADD misc/pulse-client.conf /etc/pulse/client.conf  
  
# Set the startup script  
CMD ["dumb-init", "/openvpn-firefox/entrypoint.sh"]  

