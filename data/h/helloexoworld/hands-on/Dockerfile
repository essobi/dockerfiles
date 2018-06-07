FROM warp10io/warp10:1.2.16  
ADD leveldb $WARP10_HOME/leveldb  
ADD macros $WARP10_HOME/macros  
ADD conf-standalone.conf $WARP10_HOME/etc/conf-standalone.conf  
  
WORKDIR /opt/warp10  
  
ENTRYPOINT [ "java", "-cp", "bin/warp10-1.2.16.jar:warp10-quantum-
plugin-3.0.3.jar", "io.warp10.standalone.Warp", "etc/conf-standalone.conf" ]

