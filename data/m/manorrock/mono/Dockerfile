FROM opensuse:tumbleweed  
RUN zypper addrepo
http://download.opensuse.org/repositories/Mono:Factory/openSUSE_Factory/Mono:Factory.repo
&& \  
zypper \--no-gpg-checks \--non-interactive refresh && \  
zypper \--non-interactive install mono-complete && \  
zypper removerepo
http://download.opensuse.org/repositories/Mono:/Factory/openSUSE_Factory/ && \  
zypper \--non-interactive clean -a  
WORKDIR /mnt  

