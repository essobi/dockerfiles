FROM fgagnaire/ubuntu16.10-gui:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
USER root  
MAINTAINER francis gagnaire  
  
  
  
# https://github.com/Obijuan/open-fpga-verilog-tutorial/wiki/Chapter-0%3A-you-
are-leaving-the-private-sector#ubuntu-1404-1510  
  
RUN echo "=========================================================
Installation of dependencies" \  
&& apt-get update \  
&& apt-get -y install build-essential clang bison flex libreadline-dev \  
&& apt-get -y install gawk tcl-dev libffi-dev git mercurial graphviz \  
&& apt-get -y install xdot pkg-config python python3 libftdi-dev \  
&& echo "========================================================= Installing
IceStorm Tools (icepack, icebox, iceprog) " \  
&& git clone https://github.com/cliffordwolf/icestorm.git icestorm \  
&& cd icestorm \  
&& make -j 4 \  
&& make install \  
&& echo " =========================================================
Installation of Arachne-PNR (the place & route tool)" \  
&& git clone https://github.com/cseed/arachne-pnr.git arachne-pnr \  
&& cd arachne-pnr \  
&& make -j 4 \  
&& make install \  
&& echo " =========================================================
Installation of Yosys (Verilog synthesis)" \  
&& git clone https://github.com/cliffordwolf/yosys.git yosys \  
&& cd yosys \  
&& make -j 4 \  
&& make install \  
&& apt-get -y install gtkwave iverilog \  
&& echo " ========================================================= cleaning
up stuff" \  
&& apt-get clean \  
&& ldconfig  
  
  
CMD /bin/bash  
  
  

