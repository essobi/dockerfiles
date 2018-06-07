FROM lawcab/baseimage  
MAINTAINER Lawrence Cabal <lawcab@gmail.com>  
  
#install firefox 48.0  
RUN wget https://ftp.mozilla.org/pub/firefox/releases/48.0/linux-x86_64/en-
US/firefox-48.0.tar.bz2  
RUN tar -xvjf firefox-48.0.tar.bz2 -C /opt  
RUN ln -s /opt/firefox/firefox /usr/bin/firefox  
  
#install JDK  
RUN mkdir /usr/local/java \  
&& cd /usr/local/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz \  
&& tar xvzf jdk-8u111-linux-x64.tar.gz \  
&& echo 'JAVA_HOME=/usr/local/java/jdk1.8.0_111' >> /etc/profile \  
&& echo 'PATH=$PATH:$HOME/bin:$JAVA_HOME/bin' >> /etc/profile \  
&& echo 'export JAVA_HOME' >> /etc/profile \  
&& echo 'export PATH' >> /etc/profile  
RUN update-alternatives --install "/usr/bin/java" "java"
"/usr/local/java/jdk1.8.0_111/bin/java" 1 \  
&& update-alternatives --install "/usr/bin/javaws" "javaws"
"/usr/local/java/jdk1.8.0_111/bin/javaws" 1 \  
&& update-alternatives --set java /usr/local/java/jdk1.8.0_111/bin/java \  
&& update-alternatives --set javaws /usr/local/java/jdk1.8.0_111/bin/javaws  
  
#install IntelliJ  
RUN wget https://download-cf.jetbrains.com/idea/ideaIC-2016.3.1.tar.gz \  
&& mkdir /Programs \  
&& tar xvzf ideaIC-2016.3.1.tar.gz -C /Programs \  
&& cd /Programs \  
&& mv idea* idea \  
&& mkdir /prj

