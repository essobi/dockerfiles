FROM adamant/amp  
  
USER root  
  
COPY ark-test /usr/bin  
  
# Install libstdc++ from Debian. This is an ARK/RCON dependency  
RUN cd /tmp \  
&& wget
http://ftp.de.debian.org/debian/pool/main/g/gcc-6/libstdc++6_6.3.0-18_amd64.deb
\  
&& dpkg-deb -x libstdc++6*.deb . \  
# We only need the lib files, everything else is debian junk.  
&& mv /tmp/usr/lib/x86_64-linux-gnu/libstdc++.so* /usr/lib \  
# Quickly cleanup  
&& rm -rf /tmp \  
&& install -dm1777 /tmp \  
&& chmod +rx /usr/bin/ark-test  
  
USER amp  
  
ENV MODULE=ARK \  
EXTRAS="+ARKModule.Network.GamePort 7777 +ARKModule.Network.IPBinding 0.0.0.0
+ARKModule.Server.PlayerLimit 12 +ARKModule.Network.QueryPort 27015
+ARKModule.Network.RCONPort 32330"  
  
EXPOSE 8080 7777 27015 32330  

