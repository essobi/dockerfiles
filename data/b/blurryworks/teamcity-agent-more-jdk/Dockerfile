FROM jetbrains/teamcity-agent:latest  
  
MAINTAINER Scott Markwell <scott@blurryworks.com>  
  
RUN mkdir -p /opt/build/tmp && \  
curl -o /opt/build/tmp/openjdk-9.0.4_linux-x64_bin.tar.gz
https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_linux-x64_bin.tar.gz
&& \  
tar zxvf /opt/build/tmp/openjdk-9.0.4_linux-x64_bin.tar.gz -C /usr/lib/jvm/ &&
\  
curl -o /opt/build/tmp/openjdk-10.0.1_linux-x64_bin.tar.gz
https://download.java.net/java/GA/jdk10/10.0.1/fb4372174a714e6b8c52526dc134031e/10/openjdk-10.0.1_linux-x64_bin.tar.gz
&& \  
tar zxvf /opt/build/tmp/openjdk-10.0.1_linux-x64_bin.tar.gz -C /usr/lib/jvm/
&& \  
rm -r /opt/build/tmp  
  
  
  
  
  

