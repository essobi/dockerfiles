FROM hoborg/ubuntu-dev-base:latest  
# pass in when building the image  
ARG PROXY=''  
# Proxies  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
USER root  
  
# Download and install Nodejs and NPM  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN sudo apt-get install -y nodejs  
  
# Install purescript globally  
RUN npm install -g purescript pulp bower  
  
# Switch back to user  
USER $USER  
# Install psc-package  
RUN cd $HOME  
RUN curl -L https://github.com/purescript/psc-
package/releases/download/v0.2.4/linux64.tar.gz \  
> $HOME/psc-package.tar.gz  
RUN tar xzf $HOME/psc-package.tar.gz  
RUN cp $HOME/psc-package/psc-package $HOME/.local/scripts/  
  
# Neovim plugins + settings update  
RUN cd $HOME/.homesick/repos/dotvim && git pull  
RUN cd $HOME  
RUN nvim -c 'PlugInstall' || true  
RUN nvim -c 'PlugUpdate' || true  
RUN clear # clear terminal, nvim usually garbles it  
  
CMD ["/usr/bin/zsh"]  

