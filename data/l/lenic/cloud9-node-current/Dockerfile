FROM ubuntu:latest  
  
RUN apt-get update \  
&& apt-get install -y vim git curl zsh \  
&& curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh | bash - \  
&& chsh -s /bin/zsh \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g yarn \  
&& cd /opt \  
&& git clone https://github.com/c9/core.git c9sdk \  
&& cd c9sdk \  
&& apt-get install -y make gcc \  
&& scripts/install-sdk.sh \  
&& mkdir /workspace \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /workspace  
WORKDIR /workspace  
  
EXPOSE 8181 3000  
  
ENV USERNAME admin  
ENV PASSWORD admin@123  
  
CMD node /opt/c9sdk/server.js --listen 0.0.0.0 -w /workspace -a
$USERNAME:$PASSWORD  
  

