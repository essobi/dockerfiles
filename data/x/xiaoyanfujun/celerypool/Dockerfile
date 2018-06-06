FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python openssh-server inetutils-ping
python-pip python-dev libffi-dev libssl-dev  
RUN pip install celery redis pymongo gevent pyopenssl cryptography  
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
COPY run.sh run.sh  
COPY tasks.py tasks.py  
  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

