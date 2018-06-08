FROM marcelmaatkamp/alpine-base  
  
ADD ./torrc /etc/torrc  
ADD ./tor /usr/local/bin/tor  
  
# Allow you to upgrade your relay without having to regenerate keys  
VOLUME /.tor  
  
# Generate a random nickname for the relay  
RUN echo "Nickname docker$(head -c 16 /dev/urandom | sha1sum | cut -c1-10)" >>
/etc/torrc  
  
EXPOSE 9001  
EXPOSE 9050  
EXPOSE 9053  
CMD /usr/local/bin/tor -f /etc/torrc  
  

