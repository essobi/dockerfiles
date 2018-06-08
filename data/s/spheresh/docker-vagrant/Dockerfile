FROM ubuntu:16.04  
MAINTAINER Yuriy Boychenko, yuboychenko@gmail.com  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV TERM=xterm  
  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y --no-install-recommends supervisor ssh  
  
RUN mkdir -p /var/run/sshd  
  
ARG username  
ENV USERNAME=${username:-"vagrant"}  
  
ARG userpass  
ENV USERPASS=${userpass:-"vagrant"}  
  
RUN useradd --create-home -s /bin/bash $USERNAME && \  
mkdir -p "/home/$USERNAME/.ssh" && \  
chown -R "$USERNAME:" "/home/$USERNAME/.ssh" && \  
echo -n "$USERNAME:$USERPASS" | chpasswd  
  
RUN chown -R "$USERNAME:$USERNAME" /home/$USERNAME  
  
# Enable passwordless sudo for the "vagrant" user  
RUN mkdir -p /etc/sudoers.d && \  
install -b -m 0440 /dev/null "/etc/sudoers.d/$USERNAME" && \  
echo "$USERNAME ALL=NOPASSWD: ALL" >> "/etc/sudoers.d/$USERNAME"  
  
COPY supervisor/ssh.conf /etc/supervisor/conf.d/ssh.conf  
ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon"]  
  

