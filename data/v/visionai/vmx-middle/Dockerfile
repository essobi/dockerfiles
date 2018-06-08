FROM busybox  
  
RUN mkdir -p /vmx/middle  
WORKDIR /vmx  
  
RUN \  
wget -q
http://files.vision.ai/vmx/VMXmiddle/Linux/VMXmiddle_Linux.stable.tar.gz && \  
cd middle && \  
gzip -d ../VMXmiddle_Linux.stable.tar.gz && \  
tar xf ../VMXmiddle_Linux.stable.tar && \  
rm ../VMXmiddle_Linux.stable.tar && \  
echo "Version is " `cat version`  
VOLUME /vmx/middle  

