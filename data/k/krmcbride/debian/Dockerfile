FROM debian:stretch-slim  
MAINTAINER Kevin McBride <krmcbride.io@gmail.com>  
  
# tz and vim and bash and stuff  
RUN echo "America/Los_Angeles" > /etc/timezone \  
&& /usr/sbin/dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get update && apt-get install -y \--no-install-recommends \  
vim \  
ctags \  
&& buildDeps='git ca-certificates' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone --depth=1 git://github.com/amix/vimrc.git /root/.vim_runtime \  
&& git clone --depth=1 https://github.com/Bash-it/bash-it.git /root/.bash_it \  
&& sh /root/.vim_runtime/install_basic_vimrc.sh \  
&& bash /root/.bash_it/install.sh \--silent \  
&& sed -i 's/^export BASH_IT_THEME=.\\+$/export BASH_IT_THEME=bakke/g'
/root/.bashrc \  
&& mkdir -p /usr/src/app \  
&& apt-get purge -y \--auto-remove $buildDeps  
  
WORKDIR /root  
CMD ["/bin/bash"]  

