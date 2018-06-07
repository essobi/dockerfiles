FROM fedora  
  
RUN dnf -y install 'dnf-command(copr)'; \  
dnf -y copr enable larsks/bitlbee-facebook; \  
dnf -y install \  
bitlbee \  
iproute \  
bitlbee-facebook \  
bitlbee-otr \  
; dnf clean all  
  
RUN rm -f /etc/bitlbee/bitlbee.conf  
COPY bitlbee.conf.in /etc/bitlbee/bitlbee.conf.in  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

