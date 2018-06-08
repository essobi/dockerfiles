FROM mhart/alpine-node:4  
MAINTAINER devops@signiant.com  
  
# Add our bldmgr user  
ENV BUILD_USER bldmgr  
ENV BUILD_PASS bldmgr  
ENV BUILD_USER_ID 10012  
ENV BUILD_USER_GROUP users  
  
COPY apk.packages.list /tmp/apk.packages.list  
RUN chmod +r /tmp/apk.packages.list && \  
apk --update add `cat /tmp/apk.packages.list` && \  
rm -rf /var/cache/apk/*  
  
# Install pip  
RUN cd /tmp && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python ./get-pip.py  
  
# Install PIP packages  
COPY pip.packages.list /tmp/pip.packages.list  
RUN chmod +r /tmp/pip.packages.list && \  
pip install `cat /tmp/pip.packages.list | tr \"\\\n\" \" \"`  
  
#install umpire with pre  
RUN pip install umpire --pre  
  
# install azure-cli  
RUN npm install azure-cli -g  
  
#setup user  
RUN adduser -D $BUILD_USER -s /bin/bash -G $BUILD_USER_GROUP -u $BUILD_USER_ID
&& \  
chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER && \  
echo "$BUILD_USER:$BUILD_PASS" | chpasswd  
  
RUN /usr/bin/ssh-keygen -A  
  
RUN set -x && \  
echo "UsePrivilegeSeparation no" >> /etc/ssh/sshd_config && \  
echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \  
echo "AllowGroups ${BUILD_USER_GROUP}" >> /etc/ssh/sshd_config  
  
# Comment these lines to disable sudo  
RUN apk --update add sudo && \  
rm -rf /var/cache/apk/* && \  
echo "%${BUILD_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
#setup jenkins dir  
RUN mkdir -p /var/lib/jenkins \  
&& chown -R $BUILD_USER:$BUILD_USER_GROUP /var/lib/jenkins  
  
#install packer  
RUN wget
https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip  
  
RUN mkdir /usr/local/bin/packer && \  
mkdir /home/bldmgr/goworkspace && \  
unzip packer_0.10.1_linux_amd64.zip -d /usr/local/bin/packer  
  
ENV GOROOT=/usr/lib/go  
ENV GOBIN=/usr/local/bin/packer  
ENV GOPATH=/home/bldmgr/goworkspace  
RUN export PATH=$PATH:/usr/lib/go/bin && \  
go get github.com/Azure/packer-azure/packer/plugin/packer-provisioner-azure-
custom-script-extension  
  
EXPOSE 22  
# This entry will either run this container as a jenkins slave or just start
SSHD  
# If we're using the slave-on-demand, we start with SSH (the default)  
# Default Jenkins Slave Name  
ENV SLAVE_ID JAVA_NODE  
ENV SLAVE_OS Linux  
  
ADD start.sh /  
RUN chmod 777 /start.sh  
  
CMD ["sh", "/start.sh"]  

