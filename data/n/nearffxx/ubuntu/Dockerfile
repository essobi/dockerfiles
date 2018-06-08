FROM ubuntu:18.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update \  
&& apt -y upgrade \  
&& apt -y install build-essential gcc-multilib g++-multilib binutils-multiarch
\  
&& apt -y install gdb strace ltrace netcat vim less wget git socat sudo byobu
sshpass \  
&& apt -y install python-pip python-dev \  
&& apt clean  
  
RUN git clone https://github.com/pwndbg/pwndbg \  
&& cd pwndbg \  
&& ./setup.sh \  
&& cp /root/.gdbinit /etc/gdb/gdbinit \  
&& apt clean  
  
RUN apt update \  
&& apt install -y ruby-full \  
&& apt clean  
  
RUN gem install one_gadget  
  
RUN sed -i
"1s/.*/root:\$6\$NrFUrVGe\$oATAvNu8a\/wGQRxQLp2FQsJlZQB5S5NdHB.IwPp\/hqRPd6U7eZaSaTMe7NgmDxzrEvi2B1ntWKP2GkRLRMA8T\/:17684:0:99999:7:::/"
/etc/shadow  
  
RUN pip install virtualenv  

