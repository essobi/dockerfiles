FROM ubuntu:16.04  
  
## Fixing unicode requirement error  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update && apt-get upgrade -y && DEBIAN_FRONTEND=noninteractive
apt-get install -y --no-install-recommends \  
vim-nox vim-gtk \  
screen \  
git-core git-flow \  
openssh-server openssh-client \  
tree \  
fish \  
w3m lynx  
  
# cleanup  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/  
  
# setup user  
#TODO setup user, set same permissions  
RUN addgroup --quiet --gid 1000 developer && adduser --quiet --disabled-
password --gecos "Developer" \--ingroup developer developer  
RUN chsh developer -s /usr/bin/fish  
RUN mkdir -p /home/developer/homedir  
  
# copy configs  
COPY etc/.vimrc /home/developer/.vimrc  
COPY etc/.vim /home/developer/.vim  
  
# setup running environment  
USER developer  
WORKDIR /home/developer/homedir  
ENTRYPOINT /usr/bin/fish  

