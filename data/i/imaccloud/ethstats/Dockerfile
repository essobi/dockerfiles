FROM node:5.11.0  
MAINTAINER "Kyle Bai <kyle.b@inwinstack.com>"  
# Install dependency packages  
RUN apt-get update && \  
apt-get install -y make g++ git npm  
  
# Install eth-netstats  
RUN cd /opt && \  
git clone https://github.com/cubedro/eth-netstats && \  
cd eth-netstats && \  
npm install && \  
npm install -g grunt-cli && \  
grunt  
  
COPY boot_run.sh /etc/boot_run.sh  
RUN chown root.root /etc/boot_run.sh && chmod 700 /etc/boot_run.sh  
  
# Show expose port  
EXPOSE 3000/tcp  
  
ENTRYPOINT ["/etc/boot_run.sh"]  

