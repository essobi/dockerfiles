FROM busybox  
  
RUN mkdir -p /vmx/middle  
WORKDIR /vmx/middle  
RUN \  
wget -q http://files.vision.ai/vmx/vmxAppBuilder/vmxAppBuilder.stable.tar.gz
&&\  
gzip -d vmxAppBuilder.stable.tar.gz &&\  
tar xf vmxAppBuilder.stable.tar &&\  
rm vmxAppBuilder.stable.tar &&\  
echo "Version is " `cat static/dist/version` && \  
wget -q http://files.vision.ai/vmx/VMXdocs/VMXdocs.stable.tar.gz &&\  
gzip -d VMXdocs.stable.tar.gz &&\  
tar xf VMXdocs.stable.tar -C static &&\  
echo "Version is " `cat static/docs/version` && \  
rm VMXdocs.stable.tar  
VOLUME /vmx/middle/static  
  

