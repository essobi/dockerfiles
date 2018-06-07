FROM java:8  
MAINTAINER Marc Ruiz <radykal@radykal.com>  
  
RUN wget -O /tmp/current.txt
http://jeremylong.github.io/DependencyCheck/current.txt && current=$(cat
/tmp/current.txt) && wget https://dl.bintray.com/jeremy-long/owasp/dependency-
check-$current-release.zip && unzip dependency-check-$current-release.zip &&
mv dependency-check /usr/share/  
  
VOLUME "/src /usr/share/dependency-check/data /report"  
  
ENTRYPOINT ["/usr/share/dependency-check/bin/dependency-check.sh"]  

