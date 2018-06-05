FROM ageneau/btdocker:ubuntu  
  
USER root  
  
RUN DEBIAN_FRONTEND=noninteractive sh -c '( \  
apt-get install -y -q nodejs npm && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
apt-get clean && \  
apt-get autoclean \  
)' > /dev/null  
  
RUN useradd -ms /bin/bash strong-pm \  
&& chown -R strong-pm:strong-pm /usr/local \  
&& su strong-pm -c "npm install -g strong-pm grunt-cli bower && npm cache
clear"  
  
WORKDIR /home/strong-pm  
ENV HOME=/home/strong-pm PORT=3000  
ENV NODE_ENV=docker  
  
# Run as non-privileged user inside container  
USER strong-pm  
  
# Expose strong-pm port  
EXPOSE 8701 3000  
ENTRYPOINT ["/usr/local/bin/sl-pm", "--base", ".", "--listen", "8701"]  
  

