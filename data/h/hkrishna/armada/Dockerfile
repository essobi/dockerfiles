FROM ubuntu:latest  
MAINTAINER HKrishna  
  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential gdb gdbserver && \  
apt-get install -y valgrind doxygen cmake && \  
apt-get install -y cmake && \  
apt-get install -y curl git htop man unzip vim wget && \  
apt-get install -y gawk git diffstat quilt tree && \  
apt-get install -y python python3 && \  
apt-get install -y sudo && \  
apt-get clean  
# && \  
# rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/useradd --create-home --shell /bin/bash --groups sudo hkrishna
&& \  
echo "hkrishna:hkrishna" | /usr/sbin/chpasswd  
  
# Tools  
RUN wget https://storage.googleapis.com/git-repo-downloads/repo --output-
document=/usr/bin/repo && \  
chmod a+x /usr/bin/repo  
  
# Command to run in container  
CMD ["su", "--login", "hkrishna"]  

