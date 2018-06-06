# The MIT License  
#  
# Copyright (c) 2015, CloudBees, Inc.  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in  
# all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
# THE SOFTWARE.  
FROM beevelop/cordova  
MAINTAINER Paul Römer <paul.roemer@mailbox.org>  
  
# Install and configure SSH and git  
RUN apt-get update &&\  
apt-get install -y git &&\  
apt-get install -y openssh-server &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
ENV HOME /home/jenkins  
RUN useradd -c "Jenkins user" -d $HOME -m jenkins && echo "jenkins:jenkins" |
chpasswd && chown -R jenkins.jenkins $HOME  
  
VOLUME /home/jenkins  
WORKDIR /home/jenkins  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

