FROM python:2.7.12  
MAINTAINER Kinebas Kostiantyn, https://github.com/oookotooo, version 1.0,
release latest  
  
ENV fswver 1.1.6  
WORKDIR /tmp/app  
  
# installing basic stuff (note, app does not work with python 3 on
09.09.2016):  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git  
  
#let's clone git repo  
RUN git clone -q https://github.com/internap/fake-switches.git  
  
WORKDIR /tmp/app/fake-switches  
  
# this stuff needed for python and fix insecureplatformwarning:  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-lxml python-dev
libffi-dev libssl-dev telnet telnetd python python-pip  
  
#now install pip reqiuerements:  
RUN pip install tox  
RUN pip install netaddr  
RUN pip install tftpy  
RUN pip install pycrypto  
RUN pip install Twisted  
RUN pip install pyasn1  
RUN pip install nose  
RUN pip install mock  
RUN pip install pyhamcrest  
RUN pip install pexpect  
RUN pip install flexmock  
RUN pip install ncclient  
  
#installation process in /root/fake-switches, it is long process, about 10 min
on i5  
RUN python setup.py install  
  
#fix SSHException: Signature verification (ssh-rsa) failed  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssl  
  
#switch repo to latest stable release  
RUN git checkout tags/$fswver  
  
RUN tox -r  
  
#now let's generate router (cisco for this example)  
RUN echo "from twisted.internet import reactor \n\  
from fake_switches.switch_configuration import SwitchConfiguration, Port \n\  
from fake_switches.ssh_service import SwitchSshService \n\  
from fake_switches.cisco.cisco_core import CiscoSwitchCore \n\  
\n\  
ssh_service = SwitchSshService( \n\  
ip=\"0.0.0.0\", \n\  
ssh_port=11001, \n\  
switch_core=CiscoSwitchCore(SwitchConfiguration(\"0.0.0.0\", \"my_switch\",
ports=[Port(\"FastEthernet0/1\"), Port(\"FastEthernet0/2\"),
Port(\"FastEthernet0/3\")]))) \n\  
ssh_service.hook_to_reactor(reactor) \n\  
print('Starting reactor') \n\  
reactor.run()" >> start.py  
  
#now start reactor!  
EXPOSE 11001  
ENTRYPOINT /bin/bash -c "source /tmp/app/fake-switches/.tox/py27/bin/activate
&& python /tmp/app/fake-switches/start.py"  

