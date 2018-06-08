FROM ubuntu:14.04.2  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y apache2  
RUN apt-get install -y php5 php5-curl php5-mysql php5-mcrypt php5-gd  
RUN apt-get install -y mysql-server postfix  
RUN apt-get install -y vim unzip tmux wget  
  
RUN a2enmod headers  
RUN a2enmod expires  
RUN a2enmod rewrite  
RUN php5enmod mcrypt  
  
RUN sed -ie 's/AllowOverride\ None/AllowOverride\ all/g'
/etc/apache2/apache2.conf  
RUN sed -ie 's/DocumentRoot\ \/var\/www\/html/DocumentRoot\ \/var\/www/g'
/etc/apache2/sites-available/000-default.conf  
RUN ln -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime  
  
#### VIMRC ####  
RUN echo 'set tabstop=2' >> /root/.vimrc  
RUN echo 'set shiftwidth=2' >> /root/.vimrc  
RUN echo 'set autoindent' >> /root/.vimrc  
RUN echo 'set expandtab' >> /root/.vimrc  
RUN echo 'colorscheme ron' >> /root/.vimrc  
RUN echo 'let html_no_rendering = 1' >> /root/.vimrc  
RUN echo 'syntax on' >> /root/.vimrc  
  
#### TMUX.CONF ####  
RUN echo 'set -g status-bg red' >> /root/.tmux.conf  
RUN echo 'set -g status-fg white' >> /root/.tmux.conf  
  
#### BASHRC ####  
RUN echo "service apache2 start" >> /root/.bashrc  
RUN echo "service mysql start" >> /root/.bashrc  
RUN echo "export LS_OPTIONS='--color=auto'" >> /root/.bashrc  
RUN echo "alias ls='ls \$LS_OPTIONS'" >> /root/.bashrc  
RUN echo "alias ll='ls -laF'" >> /root/.bashrc  
RUN echo "alias phpunit='phpunit --colors'" >> /root/.bashrc  

