FROM mbitz/alpinebase:e340  
MAINTAINER Howard Mei <howardmei@mubiic.com>  
  
# Add apk repository mirror list and user local bin  
COPY init /init  
COPY etc /etc  
COPY usr /usr  
COPY prep /prep  
  
RUN chmod 0755 /init /prep && NewPackages="s6 s6-portable-utils" && \  
apk-install ${NewPackages} && apk-cleanup && \  
ln -sf /bin/execlineb /usr/bin/execlineb && \  
/prep && rm -f /prep  
  
# Define the Entry Point and/or Default Command  
ENTRYPOINT ["/init"]  

