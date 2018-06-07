FROM ubuntu  
MAINTAINER Kyunam Jo <kyunam.jo@lge.com>  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list  
  
#apt update  
RUN apt update && apt -y upgrade  
  
# sudo command -y install  
RUN apt -y install sudo  
  
# Set Timezone  
ENV TZ=Asia/Seoul  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Prepare build tool  
RUN apt -y install openjdk-8-jdk  
RUN apt -y install git-core gnupg flex bison gperf build-essential zip curl
zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev
x11proto-core-dev libx11-dev lib32z-dev ccache libgl1-mesa-dev libxml2-utils
xsltproc unzip python ccache imagemagick vim net-tools gosu bc libssl-dev
locales kmod tzdata bash-completion  
  
#locale settings  
RUN locale-gen --purge en_US.UTF-8  
RUN echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale  
  
RUN apt -y install openssh-server ssh  
RUN sed -i -e "s/^#?UsePAM yes/UsePAM no/g" -e 's/^.*Port 22$/Port 22/g'
/etc/ssh/sshd_config  
  
# Adding REPO  
ADD https://storage.googleapis.com/git-repo-downloads/repo /usr/bin/repo  
RUN chmod +rx /usr/bin/repo  
  
# Clean up APT when done.  
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy create build user  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "/bin/bash"]  

