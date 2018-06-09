FROM fedora:25  
  
RUN curl -fsSL
https://github.com/spf13/hugo/releases/download/v0.20.7/hugo_0.20.7_Linux-64bit.tar.gz
| tar xz -C /usr/local/bin hugo && \  
curl -fsSL -o /etc/yum.repos.d/yarn.repo https://dl.yarnpkg.com/rpm/yarn.repo
&& \  
curl -fsSL https://rpm.nodesource.com/setup_7.x | bash - && \  
dnf install --quiet -y git openssh-clients yarn fontconfig bzip2 && \  
dnf clean all && \  
pip3 install pygments pygments-style-github  

