FROM debian:9  
  
ARG VIM_VERSION=vim80  
ARG BUILD_PACKAGES='apt-transport-https \  
sudo git vim wget curl locales procps \  
supervisor'  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y \  
&& apt-get install -yq \  
${BUILD_PACKAGES} \  
&& apt-get clean \  
# System Locale  
&& locale-gen en_US.UTF-8 \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
# Vim-Plug  
&& curl -fLo /usr/share/vim/${VIM_VERSION}/autoload/plug.vim --create-dirs \  
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  
  

