#  
# symfony-app  
#  
FROM latronchebox/php-app:php71  
MAINTAINER KUBO Atsuhiro <kubo@iteman.jp>  
  
RUN apt-get update  
RUN apt-get install -y libfile-slurp-perl nodejs npm  
  
# Install Zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& chsh -s /bin/zsh  
  
# NodeJS  
RUN npm install -g less  
  
# Apache2  
ENV APP_DOCUMENT_ROOT /var/app/web  
ADD apache2/passenv.patch /tmp/apache2-passenv.patch  
RUN patch /etc/apache2/sites-available/000-default.conf
/tmp/apache2-passenv.patch  
  
# Symfony application  
ENV APP_RUN_MODE dev  
ADD app/console /usr/local/bin/console  
RUN chmod 755 /usr/local/bin/console  
RUN chown root.root /usr/local/bin/console  
ADD app/make-app-accessible /usr/local/sbin/app-make-app-accessible  
RUN chmod 755 /usr/local/sbin/app-make-app-accessible  
RUN chown root.root /usr/local/sbin/app-make-app-accessible  
ADD app/init /tmp/app-init  
RUN cat /usr/local/sbin/app-init /tmp/app-init | sed -e 's/^#!\/bin\/bash//' >
/tmp/new-app-init  
RUN sed -i '1i #!/bin/bash' /tmp/new-app-init && cp /tmp/new-app-init
/usr/local/sbin/app-init && rm /tmp/new-app-init  

