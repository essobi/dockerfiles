FROM jaohaohsuan/jnlp-slave:latest  
RUN git clone -b master https://github.com/jaohaohsuan/inu-alpha.git \  
&& cd inu-alpha \  
&& sbt 'project root' 'release' 'clean' \  
&& sbt 'project cluster' 'compile' 'clean' 'test' 'clean' \  
&& sbt 'project frontend' 'compile' 'clean' \  
&& cd .. \  
&& tar -cvf /opt/sbt-caches.tar.gz .ivy2 .sbt \  
&& rm -rf .ivy2 .sbt inu-alpha  

