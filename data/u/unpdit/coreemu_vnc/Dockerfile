FROM ubuntu:17.10 as ipython_stage  
  
RUN apt-get -q update && apt-get install -qy python-dev python-pip  
RUN pip install -U pip  
RUN pip install pipenv  
RUN mkdir /jupyter  
WORKDIR /jupyter  
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install jupyter  
RUN /jupyter/.venv/bin/pip install jupyterlab notebook>=5.5.0 sh psutil  
  
FROM ubuntu:17.10 as emane_stage  
# Emane dependencies  
RUN apt-get update -qq  
RUN apt-get --no-install-recommends -y install wget gcc g++ autoconf automake
libtool libxml2-dev \  
libprotobuf-dev python-protobuf libpcap-dev libpcre3-dev uuid-dev debhelper
pkg-config \  
build-essential python-setuptools protobuf-compiler git dh-python python-lxml
ca-certificates  
  
# Need a patch to get EMANE to compile with GCC >7  
ADD patches/gccfix.diff /root/  
  
# Download EMANE v1.0.1 is the latest supprted  
RUN cd /root/ && wget
https://github.com/adjacentlink/emane/archive/v1.0.1.tar.gz && tar -xvf
v1.0.1.tar.gz && \  
cp gccfix.diff emane-1.0.1 && \  
cd emane-1.0.1 && patch -p1 <gccfix.diff && \  
./autogen.sh && ./configure && make deb WITHOUT_PYTHON3=1  
RUN mkdir /emane_install_debs  
RUN find /root/emane-1.0.1/.debbuild/ -iname "*.deb" -exec cp {}
/emane_install_debs \;  
  
FROM ubuntu:17.10  
ENV SCREEN_WIDTH 1280  
ENV SCREEN_HEIGHT 800  
ENV SCREEN_DEPTH 16  
ENV PASSWORD coreemu  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN apt-get update -qq && \  
apt-get install --no-install-recommends -y openbox obconf git x11vnc xvfb wget
python unzip \  
bridge-utils ebtables iproute2 iproute2 iproute libev4 libreadline6 \  
libtk-img tk8.5 dirmngr net-tools tcpdump xterm\  
feh tint2 python-numpy logrotate ca-certificates libprotobuf10 \  
socat netcat iptables \  
graphicsmagick-imagemagick-compat && \  
rm -rf /var/lib/apt/*  
  
# If we want the MDR MANET need to use the navy package  
# RUN wget https://downloads.pf.itd.nrl.navy.mil/ospf-
manet/quagga-0.99.21mr2.2/quagga-mr_0.99.21mr2.2_amd64.deb && \  
# dpkg -i quagga-mr_0.99.21mr2.2_amd64.deb && \  
# rm quagga-mr_0.99.21mr2.2_amd64.deb  
COPY packages/quagga-mr_0.99.21mr2.2_amd64.deb /tmp  
RUN dpkg -i /tmp/quagga-mr_0.99.21mr2.2_amd64.deb && rm /tmp/quagga-
mr_0.99.21mr2.2_amd64.deb  
  
RUN mkdir -p ~/.vnc  
  
RUN cd /root && git clone https://github.com/kanaka/noVNC.git && \  
cd noVNC/utils && git clone https://github.com/kanaka/websockify websockify  
  
RUN echo "deb http://eriberto.pro.br/core/ stretch main\ndeb-src
http://eriberto.pro.br/core/ stretch main" >>
/etc/apt/sources.list.d/core.list && \  
apt-key adv --keyserver pgp.surfnet.nl --recv-keys 04ebe9ef && \  
apt-get -q update && apt-get -q -y install --no-install-recommends \  
core-network core-network-daemon && apt-get -q -y install tshark \  
net-tools rox-filer \  
xorp bird openssh-client openssh-server isc-dhcp-server vsftpd apache2 tcpdump
\  
radvd at ucarp openvpn ipsec-tools racoon traceroute mgen wireshark-gtk \  
supervisor python-lxml python-protobuf && \  
rm -rf /var/lib/apt/*  
  
# We have used wireshark-gtk as that has the least dependencies but CORE
expects wireshark  
RUN ln -s /usr/bin/wireshark-gtk /usr/bin/wireshark  
  
# If we want the MDR MANET need to use the navy package  
# RUN wget https://downloads.pf.itd.nrl.navy.mil/ospf-
manet/quagga-0.99.21mr2.2/quagga-mr_0.99.21mr2.2_amd64.deb && \  
# dpkg -i quagga-mr_0.99.21mr2.2_amd64.deb && \  
# rm quagga-mr_0.99.21mr2.2_amd64.deb  
COPY \--from=emane_stage /emane_install_debs/ /tmp/emane_install_debs  
RUN dpkg -i /tmp/emane_install_debs/*.deb && rm -rf /tmp/emane_install_debs  
  
RUN cd /root/noVNC && ln -sf vnc.html index.html  
  
# Really necessary if root?  
# RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap  
ADD bg/bg.jpg /root/.config/bg.jpg  
ADD ./config/ /root/.config/  
ADD etc/supervisor/conf.d /etc/supervisor/conf.d  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
# ADD extra /extra  
VOLUME /root/shared  
# noVNC  
EXPOSE 8080  
# VNC  
EXPOSE 5900  
COPY \--from=ipython_stage /jupyter/.venv /jupyter/.venv  
# Jupyter  
EXPOSE 9999  
ENTRYPOINT "/entrypoint.sh"  

