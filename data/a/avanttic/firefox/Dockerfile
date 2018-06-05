FROM oraclelinux:6  
  
RUN yum install -y libXtst libXrender sudo firefox  
RUN yum install -y icedtea-web  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/weblogic && \  
echo "weblogic:x:${uid}:${gid}:Weblogic,,,:/home/weblogic:/bin/bash" >>
/etc/passwd && \  
echo "weblogic:x:${uid}:" >> /etc/group && \  
echo "weblogic ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/weblogic && \  
chmod 0440 /etc/sudoers.d/weblogic && \  
chown ${uid}:${gid} -R /home/weblogic  
  
USER weblogic  
ENV HOME /home/weblogic  
CMD /usr/bin/firefox  

