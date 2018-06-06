FROM ubuntu:14.04  
MAINTAINER Nikolay Golub <nikolay.v.golub@gmail.com>  
  
# Install a packages and configure SSH server  
RUN apt-get update && apt-get install -y openssh-server openjdk-7-jdk python3
python3-dev python3-pip libjpeg-dev libxml2-dev libxslt1-dev libssl-dev
libffi-dev libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 shared-mime-info git
sloccount cloc && \  
pip3 install --upgrade setuptools && \  
pip3 install --upgrade six && \  
wget https://github.com/AlDanial/cloc/releases/download/v1.70/cloc-1.70.pl -O
/usr/local/bin/cloc && chmod +x /usr/local/bin/cloc && \  
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" && \  
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \  
tar xvjf $PHANTOM_JS.tar.bz2 && \  
mv $PHANTOM_JS /usr/local/share && \  
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin && \  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd && \  
mkdir -p /var/run/sshd && \  
locale-gen en_US.UTF-8 && \  
apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/  
# Add user jenkins to the image  
RUN adduser --disabled-password --gecos "" jenkins && \  
echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
mkdir /home/jenkins/.ssh && \  
touch /home/jenkins/.ssh/authorized_keys && \  
chown -R jenkins /home/jenkins/.ssh && \  
echo "ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDmsQzUWHjrf46MZYGAs7+Ay0/koTPE1nv6Pq/E5P2u3tA9SStIZbbfz9abZc0v5m1YfPs18cZ/OJNbUilItR2IxE5w/KPvvieEsiyStNGRxcyYrBu0AMdn8zQ0avMITtJPM/+xwKeImTAApKSlUYaifUF0SAetmUhvUqZfXabps4rGp8ABdFGLzwBbTmwEbrt7z1Crk8B9un6msqBEqPGTO5P+OQAQtgbD2m1Ej5NOBOR8N3i2oLN7+C6GuRwuPXGielKG0VE1qmuaSe7hnzP3aiQDHvq2ffchQyIHPRjhmjtmGEqiPBUTDlsuRq1VZRGz27EVZ1GBi3aNezOvHInz
jenkins@1538f44c6354" >> /home/jenkins/.ssh/authorized_keys  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  

