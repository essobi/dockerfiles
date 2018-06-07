FROM judekim/ubuntu-base:14.04  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(lsb_release
-cs) main" \  
> /etc/apt/sources.list.d/launchpad-webupd8team-java.list \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true \  
| sudo debconf-set-selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true \  
| sudo debconf-set-selections && aptitude update  
  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections \  
&& aptitude install --without-recommends --assume-yes \  
oracle-java7-installer='7u65+7u60arm-0~webupd8~2' \  
oracle-java7-set-default \  
&& aptitude clean  
  
# Set JDK default env vars in /etc/environment  
RUN bash -c 'source /etc/profile.d/jdk.sh && env' | grep -E
'(PATH|(JAVA|DERBY)_HOME|J2.+?)=' | sort | tee /etc/environment  
  
RUN aptitude install --without-recommends --assume-yes \  
ant \  
&& aptitude clean  
  
# Install Maven  
RUN cd /tmp \  
&& curl http://mirrors.sonic.net/apache/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz > apache-maven-3.2.2-bin.tar.gz \  
&& curl http://www.apache.org/dist/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz.md5 > apache-maven-3.2.2-bin.tar.gz.md5 \  
&& md5sum -b apache-maven-3.2.2-bin.tar.gz | grep -q "$(cat apache-
maven-3.2.2-bin.tar.gz.md5)" \  
&& mkdir -p /opt/maven \  
&& tar -xvz --strip-components=1 -C /opt/maven -f apache-
maven-3.2.2-bin.tar.gz \  
&& rm apache-maven-3.2.2-bin.tar.gz apache-maven-3.2.2-bin.tar.gz.md5  
  
ENV PATH /opt/maven/bin:$PATH  

