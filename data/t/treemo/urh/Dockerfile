FROM ubuntu  
  
  
# upgrade image  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# install add-apt-repository command  
RUN apt-get install -y software-properties-common linux-headers-generic  
  
# RTL-SDR dependancies  
RUN apt-get install -y rtl-sdr librtlsdr-dev  
  
# bladerf dependancies  
RUN add-apt-repository ppa:bladerf/bladerf  
RUN apt-get update  
RUN apt-get install -y bladerf libbladerf-dev bladerf-firmware-fx3 bladerf-
fpga-hostedx40 bladerf-fpga-hostedx115  
  
# bladerf check  
RUN bladeRF-cli --version  
  
# install GNU radio  
RUN apt-get install -y gnuradio python-zmq  
  
# GNU radio check  
RUN uhd_fft --help  
RUN uhd_rx_cfile --help  
RUN uhd_rx_nogui --help  
  
# gqrx install  
RUN apt-get install -y gqrx-sdr  
  
# osmocom install  
RUN apt-get install -y gr-osmosdr  
  
# osmocom check  
RUN whereis osmocom_fft  
RUN whereis osmocom_siggen  
  
# install Universal Radio Hacker  
RUN apt-get install -y python3-numpy python3-psutil python3-zmq python3-pyqt5
g++ libpython3-dev python3-pip  
RUN pip3 install urh  
  
# clean / optimise docker size  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# running  
ENTRYPOINT urh  
  

