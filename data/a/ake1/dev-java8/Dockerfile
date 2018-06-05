from ake1/dev-base  
maintainer rickard@gimerstedt.se  
  
run echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
run echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
run echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
run apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
run apt-get update  
run apt-get install -y oracle-java8-installer  
  
run apt-get install -y unzip  
run wget https://services.gradle.org/distributions/gradle-2.6-all.zip  
run unzip -qq *.zip -d /usr/lib/  
run rm *.zip  
  
env JAVA_HOME=/usr/lib/jvm/java-8-oracle  
env GRADLE_HOME=/usr/lib/gradle-2.6  
env PATH=$PATH:$GRADLE_HOME/bin  
env GRADLE_OPTS=-Dorg.gradle.daemon=true  
  
# clean up  
run apt-get clean  
run rm -rf /var/lib/apt/lists/*  

