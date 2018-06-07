FROM introbay/php:7.0-apache  
MAINTAINER ignacio@introbay.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TERM xterm  
  
# Set the locale  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& sed -i -e 's/# es_ES.UTF-8/es_ES.UTF-8/' /etc/locale.gen \  
&& echo 'LANG="es_ES.UTF-8"' > /etc/default/locale \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=es_ES.UTF-8  
  
## Dev configuration  
RUN pecl install -o -f xdebug \  
&& docker-php-ext-enable xdebug  
  
COPY drupal-*.ini /usr/local/etc/php/conf.d/  
  
RUN pear channel-update pear.php.net \  
&& pear install PHP_Debug \  
&& pear install PHP_CodeSniffer-1.3.0RC1  
  
RUN apt-get update \  
&& apt-get install -y libpcre3-dev \  
&& pecl install oauth \  
&& docker-php-ext-enable oauth \  
&& rm -rf /tmp/pear \  
  
# Install development tools  
&& apt-get install -y git vim-nox exuberant-ctags \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./vimrc.local /root/.vimrc.local  
ADD ./ctags /root/.ctags  
ADD ./vimrc.before.local /root/.vimrc.before.local  
  
RUN curl http://j.mp/spf13-vim3 -L -o - | sh \  
&& vim "+PluginInstall!" "+qall" \  
&& echo "" >> /root/.bashrc \  
&& echo "source /usr/share/bash-completion/completions/git" >> /root/.bashrc \  
  
# Git  
&& git config --global color.branch auto \  
&& git config --global color.diff auto \  
&& git config --global color.status auto \  
# && git config --global user.name "Ignacio L Flores" \  
# && git config --global user.email ignacio@introbay.com \  
&& git config --global alias.st status \  
&& git config --global alias.duff 'diff --cached' \  
&& curl
https://raw.githubusercontent.com/git/git/8976500cbbb13270398d3b3e07a17b8cc7bff43f/contrib/completion/git-
prompt.sh -o ~/.git-prompt.sh \  
&& echo "source ~/.git-prompt.sh" >> /root/.bashrc \  
&& echo
"PS1='[\${debian_chroot:+(\$debian_chroot)}\\[\033[01;32m\\]\u@\h\\[\033[00m\\]:\\[\033[01;34m\\]\w\\[\033[00m\\]\$(__git_ps1
\" (%s)\")]\\\$ '" >> /root/.bashrc  
  
# Install Prestissimo  
RUN composer global require hirak/prestissimo  
  

