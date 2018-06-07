# ISLET - Runs ISLET in a container  
#  
# VERSION 1.2  
# docker run -d --name="islet" -v /usr/bin/docker:/usr/bin/docker:ro \  
# -v /var/lib/docker/:/var/lib/docker:rw -v /exercises:/exercises:ro \  
# -v /var/run/docker.sock:/var/run/docker.sock -p 2222:22 test  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
RUN apt-get update -qq  
RUN apt-get install -yq git sqlite3 pv make openssh-server supervisor  
RUN apt-get install -yq gawk vim emacs nano tcpdump rsyslog  
RUN apt-get install -yq --no-install-recommends man-db  
RUN mkdir -p /var/run/sshd /exercises  
RUN sed -i '/pam_loginuid.so/s/^/#/' /etc/pam.d/sshd  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD sshd_config /etc/ssh/sshd_config  
RUN cd /root && git clone http://github.com/jonschipp/ISLET  
RUN cd /root/ISLET && make update && make install && make user-config  
RUN cp /root/ISLET/extra/*.conf /etc/islet  
#RUN sed -i 's/docker start/sudo docker start/' /opt/islet/bin/islet_login  
#RUN sed -i 's/docker attach/sudo docker attach/' /opt/islet/bin/islet_login  
#RUN sed -i 's/docker run/sudo docker run/' /opt/islet/bin/islet_login  
ADD islet.sudoers /etc/sudoers.d/islet  
RUN chmod 0440 /etc/sudoers.d/islet  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

