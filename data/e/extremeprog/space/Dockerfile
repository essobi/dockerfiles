FROM ubuntu:14.04  
RUN apt-get update; apt-get install -y apt-transport-https; echo deb
https://deb.nodesource.com/node_4.x trusty main >> /etc/apt/sources.list  
RUN apt-get update; apt-get install -y --force-yes nodejs git ssh-client
python make g++ libkrb5-dev wget  
  
RUN npm cache clean -f; npm install -g n; n stable  
  
RUN mkdir -p /root/space  
  
RUN npm install -g bower gulp  
  
COPY package.json /root/space  
RUN cd /root/space; npm update;  
  
COPY bower.json /root/space  
RUN cd /root/space; bower update --allow-root  
  
WORKDIR /root/space  
COPY . /root/space  
RUN gulp &  
  
CMD ["bash", "/root/space/run_app.sh"]  

