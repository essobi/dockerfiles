FROM kernelci/lava-docker:2017.05  
# Add device configuration  
COPY devices/* /etc/dispatcher-config/devices/  
  
# Add device-type configuration  
COPY device-types/* /etc/lava-server/dispatcher-config/device-types/  
  
COPY scripts/setup.sh .  
  
RUN \  
/start.sh && \  
cd /root && \  
rm -rf lava-server && \  
git clone https://github.com/EmbeddedAndroid/lava-server.git -b release && \  
cd lava-server && \  
sed -i 's,dch -v ${VERSION}-1 -D unstable "Local developer build",dch -v
${VERSION}-1 -b -D unstable "Local developer build",g' /root/lava-
server/share/debian-dev-build.sh && \  
echo "cd \${DIR} && dpkg -i *.deb" >> /root/lava-server/share/debian-dev-
build.sh && \  
sed -i 's,git clone https://github.com/Linaro/pkg,git clone
https://github.com/EmbeddedAndroid/pkg,g' /root/lava-server/share/debian-dev-
build.sh && \  
/root/lava-server/share/debian-dev-build.sh -p lava-server && \  
cd /root && \  
rm -rf lava-dispatcher && \  
git clone https://github.com/EmbeddedAndroid/lava-dispatcher.git -b release &&
\  
cd lava-dispatcher && \  
/root/lava-server/share/debian-dev-build.sh -p lava-dispatcher && \  
/stop.sh  
  
COPY configs/slave/* /etc/lava-server/dispatcher.d/  
  
EXPOSE 69/udp 80 3079 5555 5556  
CMD /start.sh && /setup.sh && bash  

