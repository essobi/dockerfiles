#  
#  
#  
# pull base image.  
FROM isuper/java-oracle:jdk_8  
  
# maintainer details  
MAINTAINER Thomas Schubert "funthomas424242@gmail.com"  
# install the full configuration via puppet  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y upgrade && \  
# apt-get -y emacs && \  
apt-get install -y libgtk2.0-0 libswt-gtk-3-java puppet puppetmaster  
  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
  
ADD import.pp git.pp maven.pp eclipse.pp plugins.pp /home/developer/  
  
# install the full configuration via puppet  
RUN \  
sudo puppet apply import.pp && \  
sudo puppet apply git.pp && \  
sudo puppet apply maven.pp && \  
sudo puppet apply eclipse.pp && \  
sudo puppet apply plugins.pp  
  
  
  
# attach volumes  
# VOLUME /volume/git  
# run terminal or eclipse  
#CMD ["/bin/bash"]  
CMD /opt/eclipse/eclipse/eclipse  
  

