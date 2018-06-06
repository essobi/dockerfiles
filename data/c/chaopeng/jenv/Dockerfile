FROM centos:latest  
MAINTAINER Chao<chaopeng@chaopeng.me>  
  
RUN yum install -y unzip which && \  
yum clean all  
  
RUN curl -L -s get.jenv.io | bash && \  
source "/root/.jenv/bin/jenv-init.sh" && \  
jenv repo update && \  
jenv config auto true && \  
jenv install java 1.7.0_75 && \  
jenv clean && \  
rm -rf /root/.jenv/candidates/java/current/javafx-src.zip
/root/.jenv/candidates/java/current/src.zip
/root/.jenv/candidates/java/current/man  
  
env PATH /root/.jenv/candidates/java/current/bin:$PATH  

