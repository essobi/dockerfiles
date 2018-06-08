FROM debian:8  
# Adapted from http://www.omnicron.com/~ford/teensy/setup-teensy  
RUN PACKAGES="libusb-dev git make curl gcc-arm-none-eabi gcc unzip" && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y $PACKAGES && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV COMMIT 605d9dc91102c4fa99c1bd37ff51571e7e672773  
  
# Clone and compile teensy_loader_cli  
RUN git clone https://github.com/PaulStoffregen/teensy_loader_cli.git /loader
&& \  
(cd /loader && git reset $COMMIT \--hard && make) && \  
install -Dm755 /loader/teensy_loader_cli /usr/bin && \  
rm -rf /loader  
  
# Configure device permissions  
RUN curl -o /etc/udev/rules.d/49-teensy.rules
http://www.pjrc.com/teensy/49-teensy.rules  
  
# Download Teensy headers  
RUN curl -o /teensy.zip http://www.seanet.com/~karllunt/Teensy3xlib.zip && \  
unzip -aa -d /teensy /teensy.zip && \  
rm /teensy.zip  
  
# Apply patch  
RUN sed -i s/mk20d7/MK20D7/ /teensy/include/common.h  
  
# Copy code  
COPY . /src  
WORKDIR /src  
  
# Build  
RUN make build  
  
# Flash  
ENTRYPOINT ["make"]  
CMD ["deploy"]  

