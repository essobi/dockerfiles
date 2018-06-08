FROM ubuntu:14.04  
MAINTAINER Hajime Tazaki <thehajime@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y mercurial libexpat1-dev git-core build-essential bison
flex libssl-dev libdb-dev libpcap-dev libc6-dbg pkg-config libncurses-dev vim
bc autoconf python-pygoocanvas python-pygraphviz python-dev bzr gccxml tcpdump  
  
ADD add-defconfig /  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/ns3 && \  
echo "ns3:x:${uid}:${gid}:ns-3,,,:/home/ns3:/bin/bash" >> /etc/passwd && \  
echo "ns3:x:${uid}:" >> /etc/group && \  
echo "ns3 ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ns3 && \  
chmod 0440 /etc/sudoers.d/ns3 && \  
chown ${uid}:${gid} -R /home/ns3  
  
USER ns3  
ENV HOME /home/ns3  
  
RUN mkdir -p /home/ns3/mptcp-0.89  
WORKDIR /home/ns3/mptcp-0.89  
  
RUN git clone git://github.com/multipath-tcp/mptcp -b mptcp_v0.89  
WORKDIR /home/ns3/mptcp-0.89/mptcp  
  
RUN git remote add dce git://github.com/direct-code-execution/net-next-sim.git  
RUN git fetch dce  
RUN git config --global user.email "you@example.com"  
RUN git config --global user.name "Your Name"  
RUN git merge dce/sim-ns3-3.14.0-branch  
RUN cat /add-defconfig >> arch/sim/defconfig  
  
RUN make clean ARCH=sim  
RUN make defconfig ARCH=sim  
RUN make library ARCH=sim OPT=no  
  
WORKDIR /home/ns3/mptcp-0.89/mptcp/arch/sim/test  
RUN make testbin  
WORKDIR /home/ns3/mptcp-0.89/mptcp/  
RUN make test ARCH=sim ADD_PARAM="-r"  

