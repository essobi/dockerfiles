FROM ubuntu  
MAINTAINER Michael Bright <dockerfiles@mjbright.net>  
  
RUN apt-get update  
  
ADD .bashrc /root/.bashrc  
  
# Default command  
CMD bash  
  
# Install packages  
RUN mkdir -p /var/run/sshd  
RUN chmod 7555 /var/run/sshd  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tar build-essential curl
git-core  
  
RUN adduser --gecos "saasbook" \--disabled-password saasbook  
ADD .bashrc /home/saasbook/.bashrc  
RUN echo 'root:saasbook' |chpasswd  
RUN echo 'saasbook:saasbook' |chpasswd  
  
ADD vm-setup/configure-image-0.10.3.sh /home/saasbook/configure-
image-0.10.3.sh  
  
RUN chmod 755 /home/saasbook/configure-image-0.10.3.sh  
RUN chown saasbook:saasbook /home/saasbook/configure-image-0.10.3.sh  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install sudo  
RUN /home/saasbook/configure-image-0.10.3.sh  
  
USER saasbook  
  
#EXPOSE 22  
#EXPOSE 3000  
#ENTRYPOINT /etc/init.d/ssh start  

