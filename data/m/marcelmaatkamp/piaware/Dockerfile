FROM marcelmaatkamp/flightradar24-feeder  
  
WORKDIR /gnuradio  
RUN apt-get update && apt-get install -y tcl8.5-dev tclx8.4-dev itcl3-dev tcl-
tls tcllib automake cmake tcl-tclreadline telnet git gcc make  
RUN apt-get install -y librtlsdr-dev libusb-1.0-0-dev pkg-config debhelper
python3-dev python-virtualenv  
RUN rm -rf /usr/local/lib/librtlsdr*  
  
RUN git clone https://github.com/flightaware/piaware_builder.git  
  
WORKDIR /gnuradio/piaware_builder  
RUN ./sensible-build.sh  
  
WORKDIR /gnuradio/piaware_builder/package  
RUN dpkg-buildpackage -b  
  
ADD startPiaware.sh /gnuradio/piaware/startPiaware.sh  
  
EXPOSE 10001  
EXPOSE 30001  
EXPOSE 30002  
EXPOSE 30003  
EXPOSE 30004  
EXPOSE 30005  
EXPOSE 8080  
ENTRYPOINT /gnuradio/piaware/startPiaware.sh  

