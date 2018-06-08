FROM smeat/debian:jessie  
  
RUN apt-get update && apt-get install -y wget  
  
RUN echo deb http://packages.prosody.im/debian jessie main | tee -a
/etc/apt/sources.list  
RUN wget https://prosody.im/files/prosody-debian-packages.key -O- | apt-key
add -  
  
RUN apt-get update && apt-get install -y prosody-0.10 && apt-get purge -y
--auto-remove wget && apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sed -i '1s/^/daemonize = false;\n/' /etc/prosody/prosody.cfg.lua \  
&& perl -i -pe 'BEGIN{undef $/;} s/^log = {.*?^}$/log = {\n {levels = {min =
"info"}, to = "console"};\n}/smg' /etc/prosody/prosody.cfg.lua  
  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
CMD [ "prosody" ]  

