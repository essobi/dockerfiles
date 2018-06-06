#  
# coopermaa/fig Dockerfile  
#  
# https://github.com/coopermaa/docker-fig  
#  
FROM debian:wheezy  
MAINTAINER coopermaa77@gmail.com  
  
ENV FIGPATH /usr/local/bin/fig  
  
# Add fig binary from remote file URL  
ADD https://github.com/docker/fig/releases/download/1.0.1/fig-Linux-x86_64
$FIGPATH  
RUN chmod +x $FIGPATH  
  
WORKDIR /app  
  
# Set default application, let container to run as an executable  
ENTRYPOINT ["/usr/local/bin/fig"]  
CMD ["--help"]

