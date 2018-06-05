FROM caseywebb/interactive:latest  
MAINTAINER Casey Webb <notcaseywebb@gmail.com>  
  
RUN curl -L http://git.io/n-install | bash -s -- -y  
  
RUN zsh -c "source /root/.zshrc"  
RUN echo "local devenv=(node \$(/root/n/bin/node -v))" >> /root/.oh-my-
zsh/custom/themes/custom.zsh-theme  
  
WORKDIR /src  
  
ENTRYPOINT ["/usr/bin/zsh"]  

