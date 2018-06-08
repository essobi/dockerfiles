# LumberJack bot  
# It is difficult to dockerize this bot  
# I have no idea how to access host's screenshot  
# inside a docker container  
# Project's present status:  
# It can access mouse move inside a container  
# But due to it cannot access screenshot of the host  
# it cannot make decisions yet  
FROM ubuntu:latest  
MAINTAINER clarkzjw <clarkzjw@gmail.com>  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y firefox sudo xvfb scrot git build-essential python3
python3-dev python3-pip python3-tk  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
RUN \  
Xvfb :1 -screen 0 1366x768x16 &> xvfb.log && \  
export DISPLAY=:1.0 && \  
touch /root/.Xauthority && \  
touch /home/developer/.Xauthority && \  
pip3 install image && \  
pip3 install python3-xlib && \  
pip3 install pyautogui  
  
USER developer  
ENV HOME /home/developer  
CMD /bin/bash  

