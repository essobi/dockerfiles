FROM opensuse:tumbleweed  
RUN zypper addrepo
http://download.opensuse.org/repositories/devel:/languages:/python:/Factory/openSUSE_Tumbleweed/devel:languages:python:Factory.repo
&& \  
zypper --no-gpg-checks --non-interactive refresh && \  
zypper --non-interactive install python3 && \  
zypper removerepo
http://download.opensuse.org/repositories/devel:/languages:/python:/Factory/openSUSE_Tumbleweed/
&& \  
zypper --non-interactive clean -a  
WORKDIR /mnt  

