FROM ubuntu:xenial  
  
MAINTAINER helphi  
  
ENV LANG=C.UTF-8 \  
TZ=Asia/Shanghai  
  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y mate-desktop-environment-
core tightvncserver &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /root/.vnc &&\  
echo "123456" | vncpasswd -f > /root/.vnc/passwd &&\  
chmod 600 /root/.vnc/passwd &&\  
touch /root/.Xresources &&\  
echo "export USER=root && vncserver :1 -geometry 1366x768 -depth 24 && tail -F
/root/.vnc/*.log" > /root/start.sh  
  
EXPOSE 5901  
CMD ["sh", "/root/start.sh"]  
  
LABEL org.label-schema.docker.cmd="docker run -it -p 5901:5901
helphi/mate:xenial"

