FROM mariadb:latest  
MAINTAINER Kevin Nordloh <info@prime-host.de>  
  
RUN apt-get update && apt-get install -y openssh-server vim supervisor curl
wget git unzip zsh  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
-O - | zsh || true  
  
RUN apt-get --purge autoremove -y  
  
ADD ./my.cnf /etc/mysql/my.cnf  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Initialization and Startup Script  
RUN mkdir /root/container-scripts  
RUN mkdir /root/container-scripts/prime-host  
RUN mkdir /root/container-scripts/custom  
ADD ./mariadb-start.sh /root/container-scripts/prime-host/mariadb-start.sh  
RUN chmod 755 /root/container-scripts/prime-host/mariadb-start.sh  
  
CMD ["/root/container-scripts/prime-host/mariadb-start.sh"]  

