# set up initial container  
FROM ubuntu:14.04  
MAINTAINER Jeffrey S. Haemer "jeffrey.haemer+docker@gmail.com"  
RUN apt-get -yqq update  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
EXPOSE 22  
# create a user so I can ssh in  
ENV NEW_USER jeffrey_haemer_gmail_com  
RUN useradd -m -c 'Jeff Haemer' -s '/bin/bash' $NEW_USER  
ADD ssh /home/$NEW_USER/.ssh/  
RUN chown -R $NEW_USER:$NEW_USER /home/$NEW_USER/.ssh  
  
# default command to run if there's nothing on the command line.  
CMD [ "/bin/bash" ]  
  
# add a useful package  
RUN apt-get install -y git  

