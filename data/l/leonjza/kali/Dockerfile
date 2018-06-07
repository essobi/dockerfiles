# Kali Linux (Rolling) Docker Image  
# 2016  
#  
# Buld the image with:  
# $ docker build -t kali-rolling .  
#  
# Start a container for the first time from a built image with:  
# $ docker run -ti --name kali -h kali kali-rolling  
#  
# After the first run, start the image with:  
# $ docker start -ai kali  
FROM kalilinux/kali-linux-docker  
MAINTAINER Leon Jacobs <leonja511@gmail.com>  
  
# Let the container know there will be no TTY  
ENV DEBIAN_FRONTEND=noninteractive  
  
# From the upstream docker image  
#RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
# echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free"
>> /etc/apt/sources.list  
# Get the latest everything  
RUN apt-get -y update && \  
apt-get -y dist-upgrade  
  
# Install tools we want  
RUN apt-get install -y \  
hydra \  
john \  
metasploit-framework \  
nmap \  
sqlmap \  
wfuzz \  
exploitdb \  
nikto \  
commix \  
hashcat \  
# Wordlists  
wordlists \  
cewl  
  
# Install Other tools  
RUN apt-get install -y \  
gdb  
  
# Install utils  
RUN apt-get install -y \  
vim \  
git  
  
# Setup gdb-peda  
RUN git clone https://github.com/longld/peda.git ~/peda && \  
echo "source ~/peda/peda.py" >> ~/.gdbinit  
  
CMD ["/bin/bash"]  

