FROM busybox:ubuntu-14.04  
MAINTAINER Grafikart  
  
# Install ngrok  
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip /  
RUN unzip -o ngrok-stable-linux-amd64.zip -d /bin && \  
rm -f ngrok-stable-linux-amd64.zip  
  
#Add config script  
ADD ngrok_discover /bin/ngrok_discover  
RUN chmod +x /bin/ngrok_discover  
  
CMD ["/bin/ngrok_discover"]

