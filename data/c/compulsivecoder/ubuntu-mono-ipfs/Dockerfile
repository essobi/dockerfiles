FROM compulsivecoder/ubuntu-mono:latest  
  
RUN wget -q https://raw.githubusercontent.com/ipfs/install-go-
ipfs/master/install-ipfs.sh && \  
sh install-ipfs.sh  
  
RUN apt-get update -qq && apt-get install -qqy apt-utils apt-transport-https
ca-certificates curl  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
#RUN mkdir /.ipfs-data && \  
# cd /.ipfs-data && \  
# ipfs init  
#RUN ipfs daemon &  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  
  

