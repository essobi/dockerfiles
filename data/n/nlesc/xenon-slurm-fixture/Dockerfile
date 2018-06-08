FROM phusion/baseimage:0.9.22  
  
# become root user  
USER root  
  
# add group xenon and user xenon; create the home directory for user xenon  
RUN groupadd --system xenon && useradd --system --gid xenon --create-home
xenon  
  
# change user xenon's password to 'javagat'  
RUN echo xenon:javagat | chpasswd  
  
# become user xenon  
USER xenon  
  
# change directory into the user xenon's home directory  
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
test-fixture/links/link6  
  

