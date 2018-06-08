FROM centos:7  
  
MAINTAINER Wang, Tao <i@miffyliye.org>  
  
RUN adduser miffyliye  
  
# install rake & git & docker  
RUN yum -y install rake \  
&& yum -y install git \  
&& yum -y install docker  
  
# install dotnet core sdk  
RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc \  
&& sh -c 'echo -e "[packages-microsoft-com-prod]\nname=packages-microsoft-com-
prod \nbaseurl= https://packages.microsoft.com/yumrepos/microsoft-
rhel7.3-prod\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc"
> /etc/yum.repos.d/dotnetdev.repo' \  
&& yum -y update \  
&& yum -y install libunwind libicu \  
&& yum -y install dotnet-sdk-2.1.105  
  
# install node.js & yarn & chrome & firefox  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \  
&& yum -y install nodejs \  
&& yum -y install gcc-c++ make \  
&& curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee
/etc/yum.repos.d/yarn.repo \  
&& yum -y install yarn \  
&& yum -y install epel-release \  
&& rpm --import https://dl-ssl.google.com/linux/linux_signing_key.pub \  
&& sh -c 'echo -e "[google-chrome]\nname=google-
chrome\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-
ssl.google.com/linux/linux_signing_key.pub" > /etc/yum.repos.d/google-
chrome.repo' \  
&& yum -y update \  
&& curl --silent --location https://dl.google.com/linux/direct/google-chrome-
stable_current_x86_64.rpm --output google-chrome-stable_current_x86_64.rpm \  
&& yum -y localinstall google-chrome-stable_current_x86_64.rpm \  
&& yes | rm google-chrome-stable_current_x86_64.rpm \  
&& cd /home/miffyliye \  
&& curl --silent --location
https://ftp.mozilla.org/pub/firefox/releases/59.0.3/linux-x86_64/en-
US/firefox-59.0.3.tar.bz2 --output firefox.tar.bz2 \  
&& yum -y install bzip2 \  
&& tar xjf firefox.tar.bz2 \  
&& yes | rm firefox.tar.bz2 \  
&& chown -R miffyliye:miffyliye firefox \  
&& ln -s /home/miffyliye/firefox/firefox /usr/bin/firefox \  
&& yum -y install libXt  
  
USER miffyliye  
  
CMD /bin/bash  

