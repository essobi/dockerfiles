FROM debian:jessie  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN useradd -m build  
  
RUN apt-get update  
  
RUN apt-get install -y curl xvfb chromium \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser \  
&& chmod +x /usr/bin/xvfb-chromium  
  
RUN su build -c '\  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh |
bash \  
&& export NVM_DIR="$HOME/.nvm" \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install --lts \  
&& nvm use --lts'  
  
USER build  
  

