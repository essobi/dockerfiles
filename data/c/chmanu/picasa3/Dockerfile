FROM debian:testing  
MAINTAINER chmanu@gmail.com  
  
COPY Picasa /opt/Picasa  
ADD README /home/developer/README  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/developer && \  
echo "wine /opt/Picasa/Picasa3/Picasa3.exe" > /picasa && chmod 775 /picasa &&
\  
mkdir /home/developer/photos && mkdir /home/developer/.wine  
  
VOLUME /home/developer/photos  
VOLUME /home/developer/.wine  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
wine32-development  
  
USER developer  
ENV HOME /home/developer  
CMD /picasa  
  

