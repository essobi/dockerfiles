############################  
# Dockerfile  
# Copied from Mark Mandel  
# For Clojure  
# #########################  
  
FROM ubuntu:latest  
  
MAINTAINER Nick DeCoursin  
  
RUN apt-get -y update && \  
apt-get install -y openssh-server git gdebi wget x11-apps vim emacs software-
properties-common \  
tree xvfb xserver-xorg-core  
  
# install java  
RUN apt-get -y update && apt-get install -y openjdk-7-jre-headless  
  
#sshd setup - https://docs.docker.com/examples/running_ssh_service/  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE-now" >> /etc/profile  
EXPOSE 22  
  
#lein installation  
ENV LEIN_ROOT=1  
RUN cd /usr/local/bin && wget
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein &&
chmod +x ./lein  
  
RUN lein  
  
ADD startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
RUN mkdir /project  
WORKDIR /project  
  
#port for my web app  
ENV PORT=8080  
EXPOSE 8080  
  
ADD . /project  

