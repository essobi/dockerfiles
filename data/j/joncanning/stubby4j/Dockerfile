FROM delitescere/jdk  
  
ONBUILD ADD stubby.yml /usr/local/stubby.yml  
  
RUN wget
http://central.maven.org/maven2/by/stub/stubby4j/3.3.0/stubby4j-3.3.0.jar -O
/usr/local/stubby4j.jar  
  
CMD java -jar /usr/local/stubby4j.jar -d /usr/local/stubby.yml -l 0.0.0.0 -da
-s $STUBBY_PORT  

