FROM okadahiroshi/buildenv:artful  
  
MAINTAINER Hiroshi Okada <okadahiroshi@miobox.jp>  
  
# Install Chrome  
RUN curl -qq https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb &&\  
dpkg -i google-chrome-stable_current_amd64.deb ; apt-get --fix-broken --yes
install  
  
# Install Phantomjs  
RUN apt install -y phantomjs xvfb fonts-migmix  
  

