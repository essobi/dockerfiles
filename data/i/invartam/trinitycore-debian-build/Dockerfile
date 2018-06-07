FROM debian:jessie  
  
ADD build.sh /usr/bin/build.sh  
  
RUN chmod 755 /usr/bin/build.sh  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y cmake make git-core gcc g++ pkg-config \  
libmysqlclient-dev libssl-dev libreadline-gplv2-dev zlib1g-dev \  
libncurses5-dev libbz2-dev libpthread-workqueue-dev wget libace-dev \  
libace-6.2.8 git-core libmariadbd-dev  
RUN ln -s /lib/x86_64-linux-gnu/ /usr/lib64  
RUN ln -s /lib/x86_64-linux-gnu/librt.so.1 /lib64/  
  
VOLUME [ "/src" ]  
  
WORKDIR /src  
  
CMD [ "build.sh" ]  

