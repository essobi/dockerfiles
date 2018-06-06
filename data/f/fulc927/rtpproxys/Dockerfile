FROM fedora:latest  
MAINTAINER sebastien brice <fulc927@gmail.com>  
ENV build_date 2016-07-06 001  
# -------------------- Yum installs  
RUN dnf update -y  
#RUN dnf install -y epel-release  
RUN dnf install -y ksh bash vim  
RUN dnf install -y wireshark wget inotify-tools rsyslog ngrep tcpdump gcc
gcc-c++ bison make unzip net-tools.x86_64 mysql procps gdb iputils  
#-----------------------RTPPROXY  
RUN curl -sf -o /tmp/master.zip -L
https://github.com/sippy/rtpproxy/archive/master.zip  
RUN unzip /tmp/master.zip  
WORKDIR /rtpproxy-master  
RUN ./configure 1> /dev/null  
RUN make all  
RUN make install  
RUN rm -rf /tmp/master.zip  
RUN rm -rf /rtpproxy-master  
COPY run.sh /run.sh  
# -------------------- Kamailio configs  
RUN mkdir /sysadm  
RUN mkdir /sysadm/tmp  
ADD sys_FCT_SYS_network.sh /sysadm  
ADD sys_env.sh /sysadm  
#scripting ksh  
# Set environment variables.  
ADD .profile /root/.bashrc  
#ADD .profile /root/.kshrc  
ENV HOME /root  
# Define working directory.  
WORKDIR /root  
CMD /run.sh  

