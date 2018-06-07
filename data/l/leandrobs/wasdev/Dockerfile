FROM leandrobs/wasdev:update  
  
COPY package/7.0.0-WS-WAS-LinuxX64-FP0000031.pak maintenance/  
COPY package/7.0.0.0-WS-WASJavaSDK-LinuxX64-IFPI84269.pak maintenance/  
COPY config/install.properties responsefiles/  
RUN time { ./update.sh -options responsefiles/install.properties -silent; }  
  
WORKDIR /opt/IBM/WebSphere/AppServer  
RUN rm -rf /opt/IBM/WebSphere/UpdateInstaller /tmp/.com_ibm_tools_attach \  
/tmp/osgi_instance_location  
  

