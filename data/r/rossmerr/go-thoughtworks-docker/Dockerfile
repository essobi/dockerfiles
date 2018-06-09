FROM java:7  
ENV GO_DOWNLOAD_URL http://download01.thoughtworks.com/go/14.1.0/ga/go-
agent-14.1.0-18882.deb  
  
RUN wget -O /tmp/go-agent.deb ${GO_DOWNLOAD_URL}  
RUN dpkg -i /tmp/go-agent.deb  
RUN rm -f /tmp/go-agent.deb  
  
# get rid of GO_SERVER AND GO_SERVER_PORT defaults. We'll use env variables.  
RUN sed -i '/.*GO_SERVER.*/d' /etc/default/go-agent  
  
# make sure container doesn't exit after starting agent  
RUN sed -i 's/DAEMON=Y/DAEMON=N/' /etc/default/go-agent  
  
# make sure that init.d script passes through environment variables  
RUN sed -i 's/su -/su -p/' /etc/init.d/go-agent  
  
# set GO_SERVER env variable to go-server (defined in /etc/hosts)  
ENV GO_SERVER go-server  
  
CMD su go -c '/etc/init.d/go-agent start'

