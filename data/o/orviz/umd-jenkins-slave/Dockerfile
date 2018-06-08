FROM ubuntu:xenial  
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>  
  
RUN apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends && \  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openssh-server && \  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd && \  
mkdir -p /var/run/sshd  
  
RUN apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends openjdk-8-jre-headless && \  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins && \  
echo "jenkins:jenkins" | chpasswd  
  
RUN apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends gcc git python-dev python-setuptools
python-pip libssl-dev sudo && \  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
RUN git clone https://github.com/egi-qc/umd-verification /tmp/umd-verification
&& \  
pip install -r /tmp/umd-verification/requirements.txt  
  
RUN apt-get -q update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends python-ldap wget  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

