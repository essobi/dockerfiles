FROM ubuntu:latest  
LABEL maintainer="Kukielka <Kukielka58@gmail.com>"  
  
RUN apt-get update && \  
apt-get install -y curl build-essential git sudo screen  
  
RUN cd /tmp && \  
curl https://sh.rustup.rs --output rustup.sh && \  
chmod a+x rustup.sh && \  
sh rustup.sh -y  
  
RUN mkdir /git && \  
mkdir /node  
  
COPY docker-entrypoint.sh /  
COPY resolv.conf /tmp/resolv.conf  
  
RUN chmod a+x /docker-entrypoint.sh  
  
ENV SUDO_UID=1000  
ENV SUDO_GID=1000  
EXPOSE 53  
ENTRYPOINT ["/docker-entrypoint.sh"]

