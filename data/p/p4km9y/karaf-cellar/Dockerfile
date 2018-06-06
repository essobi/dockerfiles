FROM p4km9y/karaf  
MAINTAINER p4km9y  
  
RUN sed -i
's/^\\(featuresRepositories\s*=\s*\\).*$/\1mvn:org.apache.karaf.cellar\/apache-
karaf-cellar\/LATEST\/xml\/features, \\\/'
/opt/karaf/etc/org.apache.karaf.features.cfg; \  
sed -i 's/^\\(featuresBoot\s*=\s*\\).*$/\1cellar, \\\/'
/opt/karaf/etc/org.apache.karaf.features.cfg  
  
EXPOSE 54327/udp 4242  

