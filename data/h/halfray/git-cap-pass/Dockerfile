FROM sunteya/passenger  
MAINTAINER halfray<hui_ease@163.com>  
  
#set ssh key  
RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''  
RUN cat /root/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  
RUN chmod og-wx ~/.ssh/authorized_keys  
  
#add config file  
WORKDIR /home/app/www/shared/config  
ADD config/. .  
  
#add cap config  
WORKDIR /home/src/app/  
ADD cap/. .  
  
#install cap  
COPY Gemfile Gemfile.lock /home/src/app/  
WORKDIR /home/src/app/  
RUN bundle install  
  
#clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#add cap service  
RUN mkdir -p /etc/my_init.d  
COPY start.sh /etc/my_init.d/  
RUN chmod +x /etc/my_init.d/start.sh  

