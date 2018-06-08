# Building up Docker file for master thesis framework  
FROM ubuntu:16.04  
FROM python:2-onbuild  
MAINTAINER Martin Kraemer <info@martin-kraemer.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install apt-utils && \  
apt-get install -y \  
dnsmasq hostapd iptables network-manager net-tools rfkill tshark tcpdump \  
nano openssh-server gnome-terminal apache2 phpmyadmin\  
supervisor sudo \  
python mysql-server unzip default-jdk lib32stdc++6 lib32z1  
  
## setting up X11  
#RUN useradd -d /home/rlogin -m rlogin && echo 'rlogin:rlogin' | chpasswd  
# Replace 1000 with your user / group id  
RUN export uid=0 gid=0  
# mkdir -p /home/root && \  
# echo "root:x:${uid}:${gid}:root,,,:/home/root:/bin/bash" >> /etc/passwd && \  
# echo "root:x:${uid}:" >> /etc/group && \  
# echo "root ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/root && \  
# chmod 0440 /etc/sudoers.d/root && \  
# chown ${uid}:${gid} -R /home/root  
#USER rlogin  
#ENV HOME /home/rlogin  
## setting up ssh  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
## mysql config  
#RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
##apache & phpmyadmin  
RUN echo "Include /etc/phpmyadmin/apache.conf" >> /etc/apache2/apache2.conf  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD setup-database.sh /setup-database.sh  
ADD run.sh /run.sh  
  
RUN chmod 755 /*.sh  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql  
  
# Add volumes for the app and MySql  
VOLUME ["/var/mH-PriSe/mysql", "/var/lib/mysql"]  
VOLUME ["/home/martin/repos/docker-mhPrise/mH-PriSe-light",
"/usr/src/app/framework"]  
VOLUME ["/home/martin/repos/docker-mhPrise/conf", "/usr/src/app/config"]  
  
## setup matplot lib  
# basemap  
ENV MLP_URL https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz  
RUN curl -L ${MLP_URL} | tar xz -C /usr/local  
ENV GEOS_DIR /usr/local/  
RUN cd /usr/local/basemap-1.0.7rel/geos-3.3.3/ && ./configure
--prefix=$GEOS_DIR && make; make install  
RUN cd /usr/local/basemap-1.0.7rel/ && python setup.py install  
  
## install android  
ENV ANDROID_URL
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip  
RUN wget -q ${ANDROID_URL}  
RUN unzip tools_r25.2.3-linux.zip -d /usr/local/android/  
ENV ANDROID_HOME /usr/local/android  
  
ENV ANDROID_SDK_COMPONENTS platform-tools,build-tools-23.0.3  
RUN echo y | ${ANDROID_HOME}/tools/android update sdk --no-ui --all --filter
"${ANDROID_SDK_COMPONENTS}"  
  
ENV PATH $PATH:${ANDROID_HOME}/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools/23.0.3  
## tools  
#ADD tools/apktool /usr/local/bin/  
#ADD tools/apktool.jar /usr/local/bin/  
#RUN mkdir /opt/dex2jar/  
#ADD tools/dex2jar-2.0.zip /opt/dex2jar/  
#RUN unzip /opt/dex2jar/dex2jar-2.0.zip  
CMD ["/run.sh"]  
  
EXPOSE 3306  
EXPOSE 22  
EXPOSE 80  

