FROM ubuntu  
MAINTAINER Osbert Feng  
  
USER root  
RUN apt-get update -qq && apt-get install -qq -y python-scapy tcpdump
tcpreplay wireshark python-requests  
  
RUN useradd -m -s /bin/bash amzn-dash  
RUN echo amzn-dash:amzn-dash | chpasswd  
  
USER root  
ADD dash-listen.py /home/amzn-dash/dash-listen.py  
CMD python /home/amzn-dash/dash-listen.py  
  
# NOTE: To run this, you must link against the host networking stack  
# docker run --net=host -e DASH_MAC_ADDRESS=<use-dash-probe> -e
URL_CALLBACK=http://url/to/callback dash-listen  

