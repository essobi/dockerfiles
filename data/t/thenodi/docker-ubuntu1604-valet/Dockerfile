FROM ubuntu:16.04  
MAINTAINER Leonardo Nodari <nodarileonardo@gmail.com>  
  
# Make docker more real  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
rsyslog systemd systemd-cron sudo \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
RUN sed -i 's/^\\($ModLoad imklog\\)/#\1/' /etc/rsyslog.conf  
  
# Create user, home directory & add it to sudoers  
RUN useradd -m valet \  
&& echo "valet ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/valet  
  
# Append needed parameters to sudo env  
RUN sed -i '/Defaults env_reset/a Defaults env_keep = "COLORS DISPLAY HOSTNAME
HISTSIZE KDEDIR LS_COLORS MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE
LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES LC_MONETARY LC_NAME
LC_NUMERIC LC_PAPER LC_TELEPHONE LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET
XAUTHORITY HOME"' /etc/sudoers  
  
# Install Dependences  
RUN apt-get update \  
&& apt-get install -y nginx jq curl zip unzip git \  
php-fpm php-cli php-mcrypt php-mbstring php-xml php-curl \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ --filename=composer \  
&& mkdir /run/php  
  
# Configure environment  
RUN echo "PATH=\"\$HOME/.composer/vendor/bin:\$PATH\"" >> /home/valet/.profile
\  
&& echo 'export USER=$(whoami)' >> /home/valet/.profile  
  
# Cleanup  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Insert prepare script  
ADD prepare.sh /  
RUN chmod +x /prepare.sh  
  
CMD ["/lib/systemd/systemd"]  

