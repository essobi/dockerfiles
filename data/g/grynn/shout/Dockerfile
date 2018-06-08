# shout  
# Run shout (https://github.com/erming/shout)  
#  
# VERSION 0.0.2  
FROM grynn/node  
MAINTAINER Vishal Doshi (vishal.doshi@gmail.com)  
  
RUN git clone https://github.com/erming/shout /root/app  
WORKDIR /root/app  
RUN npm install  
RUN /usr/bin/node index.js add demo demo  
ENTRYPOINT ["/usr/bin/node", "index.js"]  
EXPOSE 9000  

