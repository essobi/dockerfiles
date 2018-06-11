FROM java:8  
  
RUN \  
wget https://bitbucket.org/yaler/yalertunnel/downloads/YalerTunnel.src.zip &&
\  
unzip YalerTunnel.src.zip && \  
javac YalerTunnel/YalerTunnel.java && \  
mv -vi YalerTunnel/YalerTunnel.class . && \  
chmod -v a+x YalerTunnel.class && \  
rm -vrf YalerTunnel/ YalerTunnel.src.zip  
  
ENTRYPOINT [ "java", "YalerTunnel" ]  

