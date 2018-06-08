# This is a comment  
FROM ubuntu:16.04  
MAINTAINER William Hilton <wmhilton@gmail.com>  
# XAMPP layers  
COPY setup-xampp.sh /root/  
RUN bash /root/setup-xampp.sh  
ENV PATH "/opt/node/bin:/opt/lampp/bin:$PATH"  
# Python layers  
COPY setup-python2.sh /root/  
RUN bash /root/setup-python2.sh  
# MailCatcher layers  
COPY setup-mailcatcher.sh /root/  
RUN bash /root/setup-mailcatcher.sh  
# SSH layers  
COPY setup-ssh.sh /root/  
RUN bash /root/setup-ssh.sh  
# Node layers  
COPY setup-node.sh /root/  
RUN bash /root/setup-node.sh  
# Rsync layers  
COPY setup-rsync.sh /root/  
RUN bash /root/setup-rsync.sh  
# XVFB layers  
COPY setup-xvfb.sh /root/  
RUN bash /root/setup-xvfb.sh  

