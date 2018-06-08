FROM opensuse:tumbleweed  
RUN zypper addrepo
http://download.opensuse.org/repositories/Java:/Factory/openSUSE_Tumbleweed/Java:Factory.repo
&& \  
zypper \--no-gpg-checks \--non-interactive refresh && \  
zypper \--non-interactive install java-10-openjdk && \  
zypper rr
http://download.opensuse.org/repositories/Java:/Factory/openSUSE_Tumbleweed/
&& \  
zypper \--non-interactive clean -a  
WORKDIR /mnt  
ENV JAVA_HOME=/usr/lib64/jvm/java-10-openjdk-10/  

