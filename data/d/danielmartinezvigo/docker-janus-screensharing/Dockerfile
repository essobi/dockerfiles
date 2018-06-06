FROM ubuntu:16.04  
MAINTAINER danielmartinezvigo  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy installation scripts in  
COPY *.sh ./  
  
# Prepare the system  
RUN chmod +x setup.sh  
RUN ./setup.sh  
  
# Install dependencies  
RUN chmod +x dependencies.sh  
RUN ./dependencies.sh  
  
# Install extras  
RUN chmod +x extras.sh  
RUN ./extras.sh  
  
# Install libsrtp 2.0.0 (To reduce risk of broken interoperability with future
WebRTC versions)  
RUN chmod +x libsrtp.sh  
RUN ./libsrtp.sh  
  
# Install usrsctp for data channel support  
RUN chmod +x usrsctp.sh  
RUN ./usrsctp.sh  
  
# Install websocket dependencies  
RUN chmod +x websockets.sh  
RUN ./websockets.sh  
  
# Clone, build and install the gateway  
RUN chmod +x janus.sh  
RUN ./janus.sh  
  
# Put configs in place  
COPY conf/*.cfg /opt/janus/etc/janus/  
RUN mkdir /opt/janus/lib/janus/events/  
  
RUN chmod -R 777 /opt/janus/  
  
# Declare the ports we use  
EXPOSE 7088 8088 7188 7989 8188 8989  
# Define the default start-up command  
RUN chmod +x startup.sh  
CMD /./startup.sh  
  
# Create Docker User  
RUN useradd -ms /bin/bash janususer  
USER janususer  
WORKDIR /home/janususer  

