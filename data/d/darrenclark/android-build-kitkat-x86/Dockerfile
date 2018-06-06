from darrenclark/android-build-base  
  
#add oracle Java 6 for KitKat builds  
run echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
  
run apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y \  
oracle-java6-installer \  
yasm \  
flex && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk6-installer  
  
  

