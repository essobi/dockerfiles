FROM ubuntu:16.04  
RUN apt-get update -q && apt-get install -y -q \  
build-essential \  
chrpath \  
cpio \  
debianutils \  
diffstat \  
gawk \  
gcc-multilib \  
git-core \  
iputils-ping \  
locales \  
python \  
python3 \  
python3-pexpect \  
python3-pip \  
socat \  
texinfo \  
tzdata \  
unzip \  
wget \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
ENV LANG en_US.utf8  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb \  
&& dpkg -i dumb-init_*.deb \  
&& rm dumb-init_*.deb  
  
RUN /usr/sbin/useradd toaster -m -s /bin/false  
  
COPY toaster-requirements.txt /tmp/  
COPY start.sh /usr/local/bin/  
  
WORKDIR /src  
  
USER toaster  
  
RUN pip3 install --user -r /tmp/toaster-requirements.txt  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/usr/local/bin/start.sh"]  

