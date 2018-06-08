FROM akihirosuda/dind-ubuntu-vivid  
MAINTAINER akihirosuda  
  
# Install OVS  
RUN apt-get update && apt-get install -y openvswitch-switch  
  
# Install Python packages  
RUN bash -c 'apt-get install -y
python-{colorama,dev,eventlet,lxml,msgpack,netaddr,networkx,oslo.config,paramiko,pip,routes,six,webob}'  
  
# Install Ryu  
RUN pip install ryu==3.20.2  
  
# Install pipework  
RUN apt-get install -y arping  
RUN wget --no-check-certificate --quiet
https://raw.githubusercontent.com/AkihiroSuda/pipework/fix-pid-
conflict/pipework -O /usr/local/bin/pipework  
RUN chmod +x /usr/local/bin/pipework  
  
# Install misc stuffs  
RUN apt-get install -y less lv netcat telnet bash-completion vim byobu  
  
# Install init  
ADD ./init.dind-ovs-ryu-pipework-superpack.sh /init.dind-ovs-ryu-pipework-
superpack.sh  
RUN chmod +x /init.dind-ovs-ryu-pipework-superpack.sh  
CMD ["wrapdocker", "/init.dind-ovs-ryu-pipework-superpack.sh"]  

