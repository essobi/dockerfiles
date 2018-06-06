FROM ubuntu:16.04  
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
force-confnew" \--no-install-recommends \  
openssh-server wget openjdk-8-jdk-headless &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
# Default command  
CMD ["/usr/sbin/sshd", "-D"]  
  
# Add Maven  
RUN wget -qO- http://apache.trisect.eu/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar xvz -C /opt  
RUN ln -s /opt/apache-maven-*/bin/mvn /usr/bin/  
  

