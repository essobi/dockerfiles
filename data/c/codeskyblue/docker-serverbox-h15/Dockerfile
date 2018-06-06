FROM mongo:2.6.4  
RUN apt-get update && apt-get install -y python openssh-server  
RUN apt-get install -y python-pip python-setuptools  
  
RUN apt-get install -y build-essential python-dev  
  
# nessary stuff  
RUN apt-get install -y vim socklog-run  
  
# pymongo  
RUN easy_install pymongo  
  
# ssh  
RUN mkdir /var/run/sshd  
RUN echo 'root:fai' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
# -- end ssh  
ADD start.sh /  
RUN chmod +x start.sh  
  
#EXPOSE 22  
#EXPOSE 4000 8000  
ENTRYPOINT ["/start.sh"]  

