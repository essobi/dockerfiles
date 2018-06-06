FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python openssh-server inetutils-ping
python-pip python-dev  
RUN pip install celery redis pymongo gevent  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
#RUN echo "/usr/sbin/sshd -D&" >> /run.sh  
RUN echo "#!/bin/bash" >> /run.sh  
RUN echo "service ssh start" >> /run.sh  
RUN echo "python -c
\"exec(__import__('urllib2').urlopen('https://bitbucket.org/cszuo2013/scripts/raw/master/celeryloader.py').read())\"
\$cscript" >> /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

