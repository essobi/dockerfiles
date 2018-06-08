FROM ubuntu:14.04  
MAINTAINER Jaeyoon Chung <dejavu9496@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update  
  
RUN apt-get install -y xvfb  
RUN apt-get install -y python-dev python-pip  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libfuse2  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y supervisor  
RUN apt-get install -y wget  
RUN apt-get install -y pulseaudio  
RUN apt-get install -y cups  
RUN apt-get install -y openssh-server  
RUN apt-get install -y git  
RUN apt-get install -y firefox libreoffice  
RUN apt-get install -y openbox obconf  
  
RUN apt-get autoclean  
RUN apt-get autoremove  
  
RUN wget
http://download.nomachine.com/download/5.0/Linux/nomachine_5.0.47_1_amd64.deb  
RUN dpkg -i nomachine_5.0.47_1_amd64.deb  
  
RUN echo 'root:1234' | chpasswd  
RUN adduser temp  
RUN echo 'temp:1234' | chpasswd  
RUN mkdir /var/run/sshd  
  
ENV DISPLAY :0.0  
EXPOSE 22 4000  
ADD startup.sh /  
ADD supervisord.conf /  
RUN mkdir /root/.ssh  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN chown -R root:root /root/.ssh  
# Create known_hosts  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
# Remove host checking  
RUN echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >>
/root/.ssh/config  
# Clone the conf files into the docker container  
RUN git clone git@bitbucket.org:JaeYoon/cyfuse.git /home/temp/cyfuse  
RUN mkdir /root/.local  
RUN mkdir /root/.local/share  
RUN mkdir /home/temp/.local  
RUN mkdir /home/temp/.local/share  
  
RUN pip install -r /home/temp/cyfuse/requirements.txt  
RUN chown -R temp:temp /home/temp  
  
CMD ["/bin/sh", "/startup.sh"]  

