FROM ubuntu:latest  
MAINTAINER tuannvm@mail.ru  
  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd && \  
mkdir -p /root/.ssh && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQCtT7vzVDoVfdXhcHH0BumQU1p/0V/ZWlqdK5+0EH4H5zRQ5nK/jKqfI83JXp5+ofwL+gTTOpyPOjehVMJu4GGco/+YCqHddZBRnz0TyDAeurmmKJO+HIMsO0lr8FSVGgqPM1Uk6H6BqWB6Xq/+HSpdVePnHaJ++CDvZdKqwihs54Ks4NuiBHK2FqZoDzg+8IXgz977yBYMrSR5wRweI5VqzBoKy9D0ag4bAvpn5Kj1z2HptYl804LyCe3VkaAguXZ286PwXHfNYzedsu6d0oSVZjD04daqQjxiKgtG2dIOt1Nw27o/uUcre5jbrKdRTMUyEh5yUnhTgQHEgdxiDNBJ
tuannvm@Tuans-MacBook-Air.local" >> /root/.ssh/authorized_keys  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

