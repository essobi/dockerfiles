FROM neubiaswg5/icy-base:latest  
  
ADD protocol.protocol /icy/protocols/protocol.protocol  
  
ADD run.sh /icy/run.sh  
  
#RUN \  
# cd /icy/plugins/adufour/blocks && \  
# wget -O Blocks.jar
http://www.bioimageanalysis.org/icy/repository/getJarFile.php?pluginId=180&beta=0
&& \  
# cd /icy/plugins/adufour/roi && \  
# wget -O ROIMeasures.jar
http://www.bioimageanalysis.org/icy/repository/getJarFile.php?pluginId=106&beta=0  
RUN cd /icy && chmod a+x run.sh  
  
ENTRYPOINT ["/bin/sh", "/icy/run.sh"]  

