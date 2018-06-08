FROM ubuntu  
  
MAINTAINER Michele Sevegnani <michele.sevegnani@glasgow.ac.uk>  
  
# Install Ubuntu packages and add prism user  
RUN apt-get -qy update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -qy --no-install-recommends install
software-properties-common \  
emacs24-nox \  
libxi6 \  
libxrender1 \  
libxtst6 \  
make \  
gcc \  
g++ && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -y -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y -qq --no-install-recommends install
oracle-java8-installer \  
oracle-java8-set-default && \  
apt-get -y -qq clean && \  
adduser --disabled-password --gecos "" prism && \  
passwd -l prism  
ADD prismsudo /etc/sudoers.d/prism  
RUN chmod 440 /etc/sudoers.d/prism && \  
chown root:root /etc/sudoers.d/prism  
  
# Install PRISM  
WORKDIR /home/prism  
ADD prism-4.3.1-src.tar.gz /home/prism/  
ADD .profile /home/prism/  
ADD .banner /home/prism/  
RUN chown -R prism:prism /home/prism/  
USER prism  
ENV HOME /home/prism  
WORKDIR /home/prism/prism-4.3.1-src  
RUN make  
  
# Configure user environment  
WORKDIR /home/prism  
ENV PATH /home/prism/prism-4.3.1-src/bin:$PATH  
  
CMD ["/bin/bash","-l"]

