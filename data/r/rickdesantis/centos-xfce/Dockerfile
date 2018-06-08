FROM centos:7  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@gmail.com>  
  
# Setting the environment  
ENV HOSTNAME centos.rickdesantis.docker.com  
ENV USERHOME /root  
ENV USER root  
ENV GEOMETRY 1440x900  
ENV PASSWORD docker  
  
WORKDIR $USERHOME  
# Update the repos and install all the used packages  
RUN yum update -y -q && \  
yum install -y -q epel-release tigervnc-server && \  
yum groupinstall -y -q "X Window system" "Xfce"  
  
# Create some useful folders  
WORKDIR ${USERHOME}  
RUN mkdir Desktop && \  
mkdir -p .config/autostart && \  
mkdir .vnc  
  
# Set the VNC server  
RUN echo $PASSWORD > password.txt && \  
cat password.txt password.txt | vncpasswd && \  
rm password.txt && \  
echo "exec /usr/bin/xfce4-session" > /etc/X11/xinit/xinitrc  
  
# Starts the VNC server  
EXPOSE 5901  
CMD vncserver :1 -desktop XFCE -geometry $GEOMETRY -depth 24 -dpi 100 && tail
-F /root/.vnc/*.log  
  
# Build: docker build -t centos1 ../centos  
# Run: docker run --name=centos1 centos1 &  
# Bash: docker exec -it centos1 bash  
# Start: docker start centos1  
# Stop: docker stop centos1  

