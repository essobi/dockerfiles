FROM iammer/dev-base  
  
RUN su -c '\  
curl https://get.sdkman.io | bash && \  
pushd $HOME/dotfiles && \  
git checkout -- bash_profile && \  
popd && \  
source "$HOME/.sdkman/bin/sdkman-init.sh" && \  
sdk install java 7u80 && \  
sdk install groovy 2.1.8 && \  
sdk install grails 2.3.4 \  
' michael  

