FROM composer/composer  
  
RUN curl -L -o /tmp/xdebug.tgz http://xdebug.org/files/xdebug-2.4.1.tgz \  
&& tar xfz /tmp/xdebug.tgz \  
&& rm -r /tmp/xdebug.tgz \  
&& mv xdebug-2.4.1 /usr/src/php/ext/xdebug \  
&& docker-php-ext-install xdebug  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y bash-completion rubygems mysql-
client libmagickwand-dev imagemagick \  
&& gem install bundler  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mcrypt \  
libjpeg-dev \  
zlib1g-dev libicu-dev g++ \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mbstring zip bcmath intl
exif fileinfo\  
&& docker-php-ext-enable opcache  
  
RUN apt-get install -y \  
pkg-config libmagickwand-dev imagemagick \  
&& curl -L -o /tmp/imagick.tgz http://pecl.php.net/get/imagick-3.4.2.tgz \  
&& tar xfz /tmp/imagick.tgz \  
&& rm -r /tmp/imagick.tgz \  
&& mv imagick-3.4.2 /usr/src/php/ext/imagick \  
&& docker-php-ext-install imagick  
  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony \  
&& chmod a+x /usr/local/bin/symfony  
  
RUN mkdir /root/composer  
  
RUN composer global require bamarni/symfony-console-autocomplete -d
/root/composer/  
  
ENV PATH "/root/composer/vendor/bin:$PATH"  
  
RUN symfony-autocomplete composer --shell bash >
/etc/bash_completion.d/composer  
  
RUN git config \--global alias.st status; \  
git config \--global alias.ci commit; \  
git config \--global alias.br branch; \  
git config \--global alias.co checkout; \  
git config \--global alias.df diff; \  
git config \--global alias.lg "log --graph --pretty=format:'%C(blue)%h
%Creset%C(reverse bold blue)%d%Creset %C(white)%s %C(green bold)%cr%Creset
%C(green)%aN' --abbrev-commit --decorate"; \  
git config \--global alias.clear '!git add -A && git reset --hard'; \  
git config \--global alias.unstage "reset HEAD --"; \  
git config \--global alias.ign "ls-files -o -i --exclude-standard"; \  
git config \--global alias.gitkconflict '!gitk --left-right
HEAD...MERGE_HEAD'; \  
git config \--global alias.alias "config --get-regexp alias"; \  
git config \--global apply.whitespace error-all; \  
git config \--global color.ui auto; \  
git config \--global color.diff.whitespace "red reverse"; \  
git config \--global color.diff.meta "magenta"; \  
git config \--global color.diff.frag "yellow"; \  
git config \--global color.diff.old "red"; \  
git config \--global color.diff.new "green bold"; \  
git config \--global color.grep.context yellow; \  
git config \--global color.grep.filename blue; \  
git config \--global color.grep.function "yellow bold"; \  
git config \--global color.grep.linenumber "cyan bold"; \  
git config \--global color.grep.match red bold; \  
git config \--global color.grep.selected white; \  
git config \--global color.grep.separator blue; \  
git config \--global color.status.added yellow; \  
git config \--global color.status.changed red; \  
git config \--global color.status.untracked "cyan bold"; \  
git config \--global diff.tool meld; \  
git config \--global instaweb.httpd 'apache2'; \  
git config \--global merge.summary true; \  
git config \--global merge.tool meld;  
  
COPY files/php.ini /usr/local/etc/php/conf.d/php.ini  
  
COPY files/bash_aliases /root/.bashrc  
  
#https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
prompt.sh  
COPY files/git-prompt.sh /root/.git-prompt.sh  
  
RUN echo "source ~/.git-prompt.sh" >> /root/.bashrc  
  
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV XDEBUG_CONFIG "idekey=session_name"  
  
ENTRYPOINT []  
  
CMD ["bash"]  

