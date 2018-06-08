# Run container in Desktop:  
# xhost +local:docker;  
# docker run --rm --name firefox54 \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY \  
# -v ~/Desktop:/home/fireuser/Desktop \  
# -v /dev/shm:/dev/shm \  
# platao/firefox54;  
# xhost -local:docker;  
FROM ubuntu:16.10  
  
# Replace 1000/100 with your user/group id  
ENV app=firefox user=fireuser uid=1000 gid=100  
  
RUN apt-get update && apt-get install -y $app  
RUN mkdir -p /home/$user && \  
echo "$user:x:$uid:$gid:$user,,,:/home/$user:/bin/bash" >> /etc/passwd && \  
echo "$user:x:$uid:" >> /etc/group && \  
mkdir -p /etc/sudoers.d && \  
echo "$user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$user && \  
chmod 0440 /etc/sudoers.d/$user && \  
chown $uid:$gid -R /home/$user  
  
USER $user  
ENV HOME /home/$user  
CMD /usr/bin/$app  

