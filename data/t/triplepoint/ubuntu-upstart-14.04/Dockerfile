FROM ubuntu:14.04  
LABEL maintainer="Jonathan Hanson (jonathan@jonathan-hanson.org)"  
  
ENV container docker  
  
# CA Certificates and openssl - support TLS  
# curl - supports some ansible fallback assumptions  
# net tools - support testinfra during role testing  
# Pip - to support reasonable python package installation  
# ssh - so we can talk to the instance with Ansible  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
net-tools \  
openssl \  
python \  
ssh \  
tzdata \  
&& rm -rf /var/lib/apt/lists/*  
  
# Make sure Pip and friends are up to the latest version.  
ADD https://bootstrap.pypa.io/get-pip.py /tmp/  
RUN python /tmp/get-pip.py \  
&& rm /tmp/get-pip.py  
  
# Upgrade the necessary components to ensure Python can handle SNI and TLS.  
RUN pip install --upgrade \  
ndg-httpsclient \  
pyasn1 \  
pyOpenSSL \  
urllib3  
  
ADD init-fake.conf /etc/init/fake-container-events.conf  
  
# undo some hacks of the base image  
RUN rm /usr/sbin/policy-rc.d; \  
rm /sbin/initctl; dpkg-divert --rename --remove /sbin/initctl  
  
# generate a nice UTF-8 locale for our use  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
  
# remove some unnecessary services  
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
; do \  
dpkg-divert --local \--rename --add "$f"; \  
done; \  
echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab  
  
# small fix for SSH in 13.10 (that's harmless everywhere else)  
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional
pam_loginuid.so/' /etc/pam.d/sshd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# set a cheap, simple password for great convenience  
RUN echo 'root:docker.io' | chpasswd  
  
# expose the SSH port  
EXPOSE 22  
CMD ["/sbin/init"]  

