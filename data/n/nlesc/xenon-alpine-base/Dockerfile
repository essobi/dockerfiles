FROM alpine:3.6  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
# Create a test user  
RUN /usr/sbin/adduser -s /bin/sh -D xenon && \  
/usr/sbin/adduser -s /bin/sh -D xenon2 && \  
  
# set user xenon's password to javagat  
echo xenon:javagat | chpasswd && \  
echo xenon2:javagat2 | chpasswd && \  
mkdir /home/xenon/.ssh && \  
mkdir /home/xenon2/.ssh  
# add ssh config directory, we need all keys to be able to do a health check
by SSH-ing to ourselves  
COPY .ssh/id_rsa.pub /home/xenon/.ssh/authorized_keys  
COPY .ssh/id_rsa /home/xenon/.ssh/id_rsa  
COPY .ssh/id_rsa.pub /home/xenon/.ssh/id_rsa.pub  
COPY .ssh/id_rsa_pw.pub /home/xenon2/.ssh/authorized_keys  
  
RUN chmod 700 /home/xenon/.ssh && \  
chmod 700 /home/xenon2/.ssh && \  
chmod 644 /home/xenon/.ssh/authorized_keys /home/xenon/.ssh/id_rsa.pub && \  
chmod 600 /home/xenon/.ssh/id_rsa && \  
chmod 644 /home/xenon2/.ssh/authorized_keys && \  
chown -R xenon.xenon /home/xenon/.ssh && \  
chown -R xenon2.xenon2 /home/xenon2/.ssh  
# use package manageer to install Bash  
RUN apk add \--no-cache bash  
  
WORKDIR /home/xenon  
# Xenon's filesystem integration tests expect certain directory structure,
create it here:  
RUN mkdir -p filesystem-test-fixture/links && \  
echo "Hello World" > filesystem-test-fixture/links/file0 && \  
touch filesystem-test-fixture/links/file1 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file0 /home/xenon/filesystem-
test-fixture/links/link0 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file1 /home/xenon/filesystem-
test-fixture/links/link1 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file2 /home/xenon/filesystem-
test-fixture/links/link2 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link0 /home/xenon/filesystem-
test-fixture/links/link3 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link2 /home/xenon/filesystem-
test-fixture/links/link4 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link6 /home/xenon/filesystem-
test-fixture/links/link5 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link5 /home/xenon/filesystem-
test-fixture/links/link6 && \  
chown -R xenon.xenon /home/xenon/filesystem-test-fixture  

