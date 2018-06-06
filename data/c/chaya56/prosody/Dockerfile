FROM ubuntu:16.10  
MAINTAINER chaya  
  
RUN apt-get update \  
&& apt-get install -y wget lsb-release \  
&& echo deb http://packages.prosody.im/debian $(lsb_release -sc) main | tee -a
/etc/apt/sources.list \  
&& wget https://prosody.im/files/prosody-debian-packages.key -O- | apt-key add
- \  
&& apt-get update \  
&& apt-get install -y lua5.2 \  
&& apt-get install -y lua-bitop \  
&& apt-get install -y prosody-0.10  
  
COPY prosody.cfg.lua /etc/prosody/prosody.cfg.lua  
  
RUN /bin/bash -c "sed -Ei
's/\$\\{PROSODY_ADMIN_USERNAME\\}/'$PROSODY_ADMIN_USERNAME'/g'
/etc/prosody/prosody.cfg.lua"  
RUN /bin/bash -c "sed -Ei
's/\$\\{PROSODY_ADMIN_PASSWORD\\}/'$PROSODY_ADMIN_PASSWORD'/g'
/etc/prosody/prosody.cfg.lua"  
RUN /bin/bash -c "sed -Ei 's/\$\\{PROSODY_SERVICE\\}/'$PROSODY_SERVICE'/g'
/etc/prosody/prosody.cfg.lua"  
RUN /bin/bash -c "sed -Ei 's/\$\\{PROSODY_MUC\\}/'$PROSODY_MUC'/g'
/etc/prosody/prosody.cfg.lua"  
  
COPY entrypoint.sh /opt/entrypoint.sh  
RUN chown -Rf prosody /opt/entrypoint.sh  
RUN chmod 755 /opt/entrypoint.sh  
  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
  
CMD ["/opt/entrypoint.sh"]  

