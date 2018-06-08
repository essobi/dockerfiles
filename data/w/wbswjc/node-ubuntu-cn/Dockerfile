FROM ubuntu:16.04  
  
RUN apt-get update -y \  
&& apt-get install curl -y \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'alias npm="npm --registry=https://registry.npm.taobao.org \  
\--cache=$HOME/.npm/.cache/cnpm \  
\--disturl=https://npm.taobao.org/dist \  
\--userconfig=$HOME/.cnpmrc"' >> ~/.bashrc  
  

