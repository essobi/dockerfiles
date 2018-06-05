ARG IMAGE=centos:7  
FROM ${IMAGE}  
  
ARG http_proxy=  
RUN yum makecache fast && yum groupinstall -y 'Development Tools' && yum
install -y m4 ruby texinfo bzip2-devel curl-devel expat-devel ncurses-devel
zlib-devel epel-release which sudo vim-enhanced curl file git python-
setuptools  
RUN groupadd --system --non-unique -g 999 docker && groupadd -g 1000 linuxbrew  
RUN groupadd --system sudo && mkdir -m 0755 -p /etc/sudoers.d && echo '%sudo
ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/99-sudo && chmod 0440
/etc/sudoers.d/99-sudo && sed -i -E -e
's/Defaults\s+requiretty/Defaults\t!requiretty/g' /etc/sudoers  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
ADD run.sh /  
VOLUME ["/home/linuxbrew"]  
#WORKDIR /home/linuxbrew  
#USER linuxbrew  
#ENV HOME=/home/linuxbrew  
#ENV BREWBIN=$HOME/.linuxbrew/bin/brew  
#RUN git clone https://github.com/Homebrew/linuxbrew.git $HOME/.linuxbrew  
#ENV HOMEBREW_BUILD_FROM_SOURCE=1 PATH=$HOME/.linuxbrew/bin:$PATH  
#RUN .linuxbrew/bin/brew update || .linuxbrew/bin/brew update  
#RUN .linuxbrew/bin/brew tap ambakshi/formulae  
#RUN .linuxbrew/bin/brew install brew-fpm  
#RUN .linuxbrew/Library/Homebrew/vendor/portable-ruby/2.3.3/bin/gem install
--no-rdoc --no-ri fpm  
#RUN mkdir -p $HOME/.local/bin $HOME/bin  
#RUN ln -sfrn $HOME/.linuxbrew/Library/Homebrew/vendor/portable-
ruby/2.3.3/bin/fpm $HOME/.local/bin/  
CMD ["/run.sh"]  

