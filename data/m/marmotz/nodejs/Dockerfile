FROM marmotz/debian-fr  
  
USER root  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Install watchman  
RUN cd / && \  
git clone https://github.com/facebook/watchman.git && \  
cd watchman && \  
git checkout v4.7.0 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  
  
ADD init_nodejs.sh /  
ADD launch_nodejs.sh /  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
USER nonrootuser  
  
EXPOSE 80  
VOLUME ["/data"]  
WORKDIR /data  
  
CMD ["/launch_nodejs.sh"]  

