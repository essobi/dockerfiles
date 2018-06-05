FROM caseywebb/interactive:latest  
MAINTAINER Casey Webb <notcaseywebb@gmail.com>  
  
RUN apt-get -y install \  
python \  
python-setuptools \  
python-notify \  
python-chardet \  
intltool \  
python-xdg \  
xdg-utils  
  
RUN zsh -c "source /root/.zshrc"  
RUN echo "local devenv=(\$(/usr/bin/python --version 2>&1))" >> /root/.oh-my-
zsh/custom/themes/custom.zsh-theme  
  
WORKDIR /src  
  
ENTRYPOINT ["/usr/bin/zsh"]  

