FROM ubuntu:latest  
  
MAINTAINER tattsun <t.t.mc1192.sf@gmail.com>  
  
  
RUN apt-get update  
  
# install tools  
RUN apt-get -y install git sudo passwd vim python-setuptools  
  
# install sshd  
RUN apt-get -y install openssh-server  
  
# install supervisor  
RUN easy_install supervisor  
  
# cleaning apt-get  
RUN apt-get clean  
  
# configure sshd  
RUN mkdir /var/run/sshd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# change here  
RUN echo 'root:hoge' | chpasswd  
  
# configure supervisor  
RUN echo_supervisord_conf > /etc/supervisord.conf  
RUN echo '[include]' >> /etc/supervisord.conf  
RUN echo 'files = supervisord/conf/*.conf' >> /etc/supervisord.conf  
RUN mkdir -p /etc/supervisord/conf/  
ADD supervisor.conf /etc/supervisord/conf/service.conf  
  
EXPOSE 22 80  
CMD ["supervisord", "-n"]  

