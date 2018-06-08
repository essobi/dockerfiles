FROM ubuntu:14.04  
MAINTAINER Khlebnikov Andrey <viruszold@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y software-properties-common
python-software-properties openssh-server  
RUN apt-get update -qq && \  
apt-get install -qq cmake g++-4.8 libboost1.55-all-dev libboost-log1.55-dev
libcairo2-dev libpng12-dev asciidoc git  
RUN mkdir ~/src && cd ~/src && git clone https://github.com/alacarte-
maps/alacarte.git && \  
cd alacarte && mkdir build && cd build && cmake .. -DBUILD_TESTING=NO
-DCMAKE_BUILD_TYPE=Release && make  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22 80 8080 443 3000  
CMD ["/usr/sbin/sshd", "-D"]

