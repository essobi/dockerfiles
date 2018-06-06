FROM cantara/zulu  
MAINTAINER Totto <totto@totto.org>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openssh-server apache2 supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install sshd - should probably be fortified  
RUN mkdir -p /var/run/sshd  
RUN echo 'root:kjempehemmelig' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN /usr/bin/ssh-keygen -f /root/.ssh/id_rsa  
  
ENV USER=UserIdentityBackend  
ENV HOME=/home/$USER  
RUN useradd -d "$HOME" -u 500 -m -s /bin/bash $USER  
  
## Install UserIdentityBackend  
COPY testdata/* $HOME/testdata/  
COPY toRoot/* $HOME/  
RUN chown -R $USER:$USER $HOME  
RUN chmod 755 $HOME/*.sh  
RUN su - $USER -c "$HOME/update-service.sh"  
#RUN su - $USER -c "$HOME/start-service.sh &"  
## Install Apache and set up proxypasses  
RUN a2enmod proxy_http  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
RUN /usr/bin/wget -O /etc/apache2/sites-available/whydah.conf -q -N
https://raw.githubusercontent.com/cantara/Whydah/master/config/apache/whydah.conf  
RUN ln -s ../sites-available/whydah.conf /etc/apache2/sites-
enabled/whydah.conf  
  
## Set up start of services  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 22 80 9999  
CMD ["/usr/bin/supervisord"]  

