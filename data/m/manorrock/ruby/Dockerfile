FROM opensuse:tumbleweed  
RUN zypper addrepo
http://download.opensuse.org/repositories/devel:/languages:/ruby/openSUSE_Tumbleweed/devel:languages:ruby.repo
&& \  
zypper --no-gpg-checks --non-interactive refresh && \  
zypper --non-interactive install ruby && \  
zypper removerepo
http://download.opensuse.org/repositories/devel:/languages:/ruby/openSUSE_Tumbleweed/
&& \  
zypper --non-interactive clean -a  
WORKDIR /mnt  
  

