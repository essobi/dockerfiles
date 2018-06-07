FROM haugene/transmission-openvpn  
MAINTAINER Robert Deuser  
  
ADD /start.sh /start.sh  
RUN chmod u+x /start.sh  
  
RUN sudo apt-get update  
RUN sudo apt-get upgrade -y  
RUN sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-
dev libffi-dev python-pip python-dev libssl-dev git -y  
RUN sudo apt-get install unrar-free  
  
RUN sudo pip install pyopenssl==0.13.1  
RUN sudo git clone https://github.com/SickRage/SickRage.git /etc/sickrage  
  
EXPOSE 8081  
CMD ["dumb-init", "/start.sh"]  

