# Note: The newer busybox:glibc is missing libpthread.so.0.  
FROM busybox:ubuntu-14.04  
# Install ngrok (latest official stable from https://ngrok.com/download).  
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
/ngrok.zip  
RUN set -x \  
&& unzip -o ngrok.zip -d /bin \  
&& rm -f /ngrok.zip  
  
# Create non-root user.  
RUN set -x \  
&& echo 'ngrok:x:6737:6737:Ngrok user:/home/ngrok:/bin/false' >> /etc/passwd \  
&& echo 'ngrok:x:6737:' >> /etc/group \  
&& mkdir -p /var/lib/ngrok \  
&& chown ngrok:ngrok /var/lib/ngrok \  
&& chmod 700 /var/lib/ngrok  
  
USER ngrok  
  
ENTRYPOINT ["/bin/ngrok"]  

