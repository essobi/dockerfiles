FROM debian:jessie  
  
ENV SRC_REPO=/root/lsyncd  
  
RUN apt-get update \  
&& apt-get install -y ssh rsync git cmake build-essential lua5.2 liblua5.2-dev
\  
&& git clone https://github.com/axkibe/lsyncd.git $SRC_REPO \  
&& cd $SRC_REPO \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr/local \  
&& make \  
&& make install \  
&& apt-get remove -y git cmake build-essential \  
&& apt-get autoremove -y \  
&& apt-get autoclean \  
&& mkdir /root/.ssh  
  
CMD lsyncd -insist -nodaemon -log scarce $CONFIG  

