FROM mongo:3.0.1  
MAINTAINER Justin Grant "http://www.justinleegrant.com"  
# update apt  
RUN apt-get update  
  
# install ssh  
RUN apt-get install -y openssh-server  
  
# supervisor installation  
RUN apt-get -y install supervisor  
  
# create ssh dir and set password  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# install python pip  
RUN apt-get install -y python-pip  
  
# create directory for child images to store configuration in  
RUN mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
# supervisor base configuration  
ADD conf/supervisor.conf /etc/supervisor.conf  
  
# additional configurations  
ADD conf/mongod.conf /etc/supervisor/conf.d/mongod.conf  
ADD conf/sshd.conf /etc/supervisor/conf.d/sshd.conf  
ADD conf/bootstrap.conf /etc/supervisor/conf.d/bootstrap.conf  
  
# add bootstrap files for loading  
ADD test-data.js /bootstrap/data/test-data.js  
  
# expose the ports (mongodb is already exposed)  
EXPOSE 22  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  

