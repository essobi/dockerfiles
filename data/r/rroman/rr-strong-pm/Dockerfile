FROM node:4.2  
RUN apt-get update && \  
apt-get install -y libkrb5-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash strong-pm \  
&& chown -R strong-pm:strong-pm /usr/local \  
&& su strong-pm -c "npm install -g strong-pm && npm cache clear"  
  
# Set up some semblance of an environment  
WORKDIR /home/strong-pm  
ENV HOME=/home/strong-pm PORT=3000  
# Run as non-privileged user inside container  
USER strong-pm  
  
# Expose strong-pm port  
EXPOSE 8701 3000 3001 3002 3003 3004  
ENTRYPOINT ["/usr/local/bin/sl-pm", "--base", ".", "--listen", "8701"]  

