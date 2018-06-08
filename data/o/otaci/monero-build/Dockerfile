# This Dockerfile is used to build an image containing everything needed to
build and test Monero on a Jenkins slave build node.  
# adapted from https://hub.docker.com/r/evarga/jenkins-slave/  
FROM ubuntu:latest  
MAINTAINER Otaci  
  
# In case you need proxy  
#RUN echo 'Acquire::http::Proxy "http://127.0.0.1:8080";' >> /etc/apt/apt.conf  
  
# Add locales after locale-gen as needed  
# Upgrade packages on image  
# Preparations for sshd  
run locale-gen en_US.UTF-8 &&\  
apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# install dependencies  
RUN apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends git build-essential cmake pkg-config
libboost-all-dev libssl-dev libunbound-dev libminiupnpc-dev libunwind8-dev
liblzma-dev libldns-dev libexpat1-dev doxygen graphviz cloc &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y libgtest-dev && cd
/usr/src/gtest && cmake . && make && mv libg* /usr/lib &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  

