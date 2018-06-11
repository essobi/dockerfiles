FROM ubuntu:16.04  
RUN apt-get update && apt-get install \  
vim \  
git \  
make \  
zsh \  
wget \  
curl \  
tzdata \  
-y && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)";exit 0  
RUN chsh -s /bin/zsh  
COPY sources.list /etc/apt/sources.list  
COPY kuishell.zsh-theme /root/.oh-my-zsh/themes/  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
WORKDIR /root  
CMD zsh  

