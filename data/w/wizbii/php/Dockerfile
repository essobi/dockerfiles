FROM wizbii/php:apache  
  
ENV container docker  
  
RUN apt-get update && apt-get install -y systemd && rm -rf
/var/lib/apt/lists/* && \  
find /etc/systemd/system \  
/lib/systemd/system \  
-path '*.wants/*' \  
-not -name '*journald*' \  
-not -name '*systemd-tmpfiles*' \  
-not -name '*systemd-user-sessions*' \  
-exec rm \\{} \;  
  
RUN systemctl set-default multi-user.target  
  
STOPSIGNAL SIGRTMIN+3  
  
ENTRYPOINT ["bash", "-c" , "exec /bin/systemd $(env | grep -v \" \" |while
read env ; do echo -n \"systemd.setenv=${env} \"; done)"]  

