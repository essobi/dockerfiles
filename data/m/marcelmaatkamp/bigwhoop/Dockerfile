FROM marcelmaatkamp/gnuradio:3.7.1  
WORKDIR /gnuradio  
  
# ---  
# libraries  
RUN apt-get install -y python-setuptools python-dev build-essential python-pip
gettext-base  
RUN pip install pyrtlsdr  
  
# ---  
# code  
RUN git clone https://github.com/aerospaceresearch/DGSN_bigwhoop.git  
WORKDIR /gnuradio/DGSN_bigwhoop/node  
  
# ---  
# add startup script  
ADD bin/start_bigwhoop.sh /gnuradio/DGSN_bigwhoop/node/start_bigwhoop.sh  
  
# ---  
# external configuration mount  
VOLUME /gnuradio/DGSN_bigwhoop/node/config  
  
# ---  
# startup script  
ENTRYPOINT ./start_bigwhoop.sh  

