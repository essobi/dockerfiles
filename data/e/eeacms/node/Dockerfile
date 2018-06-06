FROM node:4.2.2  
RUN apt-get update -q && \  
apt-get install python3-pip -y && \  
apt-get upgrade -y libc6 libc6-dev && \  
pip3 install chaperone && apt-get clean && rm -rf /tmp/* /var/tmp/*
/var/lib/apt/lists/*  
  
RUN useradd -m node && usermod -u 600 node  
RUN mkdir -p /external_templates  
RUN chown node:node -R /external_templates  
ENTRYPOINT ["/usr/local/bin/chaperone", "/code/app.js"]  
CMD ["runserver"]  

