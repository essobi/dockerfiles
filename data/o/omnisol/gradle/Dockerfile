FROM openjdk:8  
  
ARG user=gradle  
ARG group=gradle  
ARG uid=1000  
ARG gid=1000  
  
ENV GRADLE_USER_HOME /home/$user  
RUN apt-get update && apt-get install -y openjfx \  
&& groupadd -g $gid $group \  
&& useradd -d $GRADLE_USER_HOME -u $uid -g $group -s /bin/bash $user \  
&& mkdir -p $GRADLE_USER_HOME \  
&& chown -R $user:$group $GRADLE_USER_HOME  
RUN ln -fs /usr/share/zoneinfo/Asia/Jerusalem /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
USER $user  
  
VOLUME $GRADLE_USER_HOME  

