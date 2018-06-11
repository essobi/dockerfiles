FROM dockerfile/ubuntu  
  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-unstable && \  
rm -rf /var/lib/apt/lists/*  
  
# Create a user  
RUN adduser chrome  
  
USER chrome  
ENV HOME /home/chrome  
  
CMD []  
ENTRYPOINT ["/usr/bin/google-chrome-unstable", "--no-sandbox"]

