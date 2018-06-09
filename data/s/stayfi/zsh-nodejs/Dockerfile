FROM debian:jessie  
MAINTAINER Stayfi B. <stayfi@gmail.com>  
  
RUN apt-get update -y \  
&& apt-get install -y zsh git curl vim sudo \  
&& curl https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh | bash \  
&& sed -i -- 's/ZSH_THEME="robbyrussell"/ZSH_THEME="gallois"/g' /root/.zshrc \  
&& sed -i -- 's/plugins=(git)/plugins=(git node npm bower)/g' /root/.zshrc \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs \  
&& mkdir -p /root/.config/configstore \  
&& chmod g+rwx /root /root/.config /root/.config/configstore \  
&& npm install -g \--silent yo \--allow-root bower \--allow-root gulp grunt-
cli angular-cli \  
&& rm -rf /var/lib/apt/lists/* \  
&& chsh -s /usr/bin/zsh \  
&& adduser \--disabled-password \--gecos "" yeoman \  
&& echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ENV SHELL /usr/bin/zsh  
  
EXPOSE 8000  
  
WORKDIR /var/www  
  
ENTRYPOINT /usr/bin/zsh

