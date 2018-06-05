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
apt-get install -y libgtk2.0-0 libswt-gtk-3-java puppet puppetmaster firefox  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
mkdir -p /home/developer/.local/share/applications && \  
mkdir -p /home/developer/Schreibtisch/ && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
  
ADD import.pp git.pp spring-sts.pp permissions.pp /home/developer/  
  
# install the full configuration via puppet  
RUN \  
sudo puppet apply import.pp && \  
sudo puppet apply git.pp && \  
sudo puppet apply spring-sts.pp && \  
sudo puppet apply permissions.pp  
  
# attach volumes  
# VOLUME /volume/git  
  
EXPOSE 8080  
  
# run terminal or spring-sts  
#CMD ["/bin/bash"] sh -c '<command1 && command2 [&& command3 [...]]>'  
CMD /home/developer/installationen/sts/STS  
  

