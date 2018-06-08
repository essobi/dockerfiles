##########################################################################  
# Machination  
# Copyright (c) 2014, Alexandre ACEBEDO, All rights reserved.  
#  
# This library is free software; you can redistribute it and/or  
# modify it under the terms of the GNU Lesser General Public  
# License as published by the Free Software Foundation; either  
# version 3.0 of the License, or (at your option) any later version.  
#  
# This library is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU  
# Lesser General Public License for more details.  
#  
# You should have received a copy of the GNU Lesser General Public  
# License along with this library.  
##########################################################################  
  
FROM ubuntu:trusty  
ENV user vagrant  
  
RUN apt-get update -y  
RUN apt-get install wget ssh -y  
  
RUN useradd -m $user  
RUN echo "$user:$user" | chpasswd  
RUN mkdir -p /home/$user/.ssh  
RUN wget
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub -O
/home/$user/.ssh/authorized_keys  
RUN chown -R $user:$user /home/$user/.ssh  
RUN chmod 700 /home/$user/.ssh  
RUN chmod 600 /home/$user/.ssh/authorized_keys  
RUN echo "$user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN mv /sbin/dhclient /usr/sbin/dhclient  
  
# Stuff coming from upstart image for docker
(https://registry.hub.docker.com/u/library/ubuntu-upstart/)  
ADD init-fake.conf /etc/init/fake-container-events.conf  
RUN rm /usr/sbin/policy-rc.d; rm /sbin/initctl; dpkg-divert --rename --remove
/sbin/initctl  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
RUN /usr/sbin/update-rc.d -f ondemand remove; \  
for f in \  
/etc/init/u*.conf \  
/etc/init/mounted-dev.conf \  
/etc/init/mounted-proc.conf \  
/etc/init/mounted-run.conf \  
/etc/init/mounted-tmp.conf \  
/etc/init/mounted-var.conf \  
/etc/init/hostname.conf \  
/etc/init/networking.conf \  
/etc/init/tty*.conf \  
/etc/init/plymouth*.conf \  
/etc/init/hwclock*.conf \  
/etc/init/module*.conf\  
; do dpkg-divert --local --rename --add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN echo 'root:root' | chpasswd  
  
EXPOSE 22  
  
  
CMD ["/sbin/init"]  

