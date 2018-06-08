FROM debian:jessie  
  
# Setup Repo  
COPY apt.sources.list.debian /etc/apt/sources.list  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys D57D95AF93178A7C && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 7DE089671804772E  
  
RUN apt-get update  
  
# Copy over install scripts  
RUN mkdir -p /tmp  
  
COPY packages/app-packages.txt /tmp/  
RUN cd /tmp && apt-get install -y $(grep -vE "^\s*#" app-packages.txt | tr
"\n" " " )  
  
COPY packages/app-packages-testing.txt /tmp/  
RUN cd /tmp && apt-get -t testing install -y $(grep -vE "^\s*#" app-packages-
testing.txt | tr "\n" " " )  
  
COPY packages/packages.txt /tmp/  
RUN cd /tmp && apt-get install -y $(grep -vE "^\s*#" packages.txt | tr "\n" "
")  
  
COPY scripts/*.sh /tmp/  
RUN /tmp/buck.sh  
RUN /tmp/node.sh  
RUN /tmp/lfs.sh  
RUN /tmp/curl.sh --host=arm-linux-gnueabihf  
RUN /tmp/lcm.sh --host=arm-linux-gnueabihf  

