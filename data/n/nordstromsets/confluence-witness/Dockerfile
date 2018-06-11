FROM python:2.7.9  
MAINTAINER Tom Jackson thomas.jackson@nordstrom.com  
  
# Provides a simple witness server that the Confluence ELB can use to assess
if Confluence  
# on this instance is currently "primary".  
# ELB goal is:  
# route 100% of traffic to R/W node if R/W is up, and  
# route 100% of traffic to R/O if R/W is not up and R/O node is up  
# Port to run the witness on  
ENV WITNESS_PORT 8090  
# IP Address of Confluence R/W server  
# This must be set via docker run  
ENV CONFLUENCE_RW_IP TBD  
  
# IP Address of the container host  
# This must be set via docker run  
ENV CONTAINER_HOST_IP TBD  
  
# Define env variables that will allow the docker builder to navigate the  
# outbound proxy. Note that these are only needed if building this image  
# behind our firewall.  
# ENV http_proxy http://pbcld-proxy.nordstrom.net:3128  
# ENV https_proxy https://pbcld-proxy.nordstrom.net:3128  
# ENV no_proxy localhost,10.0.0/8,nordstrom.net  
# install required python packages  
RUN easy_install web.py  
RUN pip install requests  
RUN pip install docker-py  
  
# add the web server to /usr/local  
# make home dir for the server  
RUN mkdir -p /usr/local/witness-server/lib  
  
# add the witness server files  
ADD witness-server.py /usr/local/witness-server/witness-server.py  
ADD lib/ /usr/local/witness-server/lib/  
  
# Run server under the default unprivileged account. This could be considered
bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
# Note: this must be done before the volumes below are created  
USER daemon:daemon  
  
# Set the working directory install dir  
WORKDIR /usr/local/witness-server  
  
# Export the server port  
EXPOSE 8090  
# run server in the foreground  
CMD python -m witness-server $WITNESS_PORT $CONTAINER_HOST_IP
$CONFLUENCE_RW_IP  

