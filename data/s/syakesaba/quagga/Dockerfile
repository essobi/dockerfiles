FROM debian  
MAINTAINER SYA-KE  
  
RUN apt-get update -y && apt-get install -y \  
git gcc build-essential automake autoconf libtool m4 vim telnet net-tools gawk
\  
libreadline-dev texinfo  
RUN git clone git://git.savannah.nongnu.org/quagga.git  
RUN cd quagga && ./bootstrap.sh && ./configure && make install  
RUN mkdir /etc/quagga  
RUN find / -name daemons  
RUN for f in /usr/local/etc/*.conf.sample;do cp $f /etc/quagga/`basename
${f%.sample}`;done  
RUN touch /etc/quagga/daemons  
RUN echo "bgpd=yes" >> /etc/quagga/daemons  
RUN echo "isisd=yes" >> /etc/quagga/daemons  
RUN echo "ospfd6=yes" >> /etc/quagga/daemons  
RUN echo "ospfd=yes" >> /etc/quagga/daemons  
RUN echo "pimd=yes" >> /etc/quagga/daemons  
RUN echo "ripd=yes ">> /etc/quagga/daemons  
RUN echo "ripngd=yes" >> /etc/quagga/daemons  
RUN echo "vtysh=yes" >> /etc/quagga/daemons  
RUN echo "zebra=yes" >> /etc/quagga/daemons  
ENTRYPOINT ["/bin/bash"]  

