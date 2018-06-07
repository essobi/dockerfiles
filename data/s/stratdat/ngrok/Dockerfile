FROM busybox:ubuntu-14.04  
MAINTAINER Adam Clarke <adamc@strategicdata.com.au>  
  
# Install ngrok  
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
/ngrok.zip  
RUN unzip -o ngrok.zip -d /bin && \  
rm -f ngrok.zip  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

