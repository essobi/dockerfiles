## Dockerfile for "base" Debian image.  
## This image contains some utilities that I can reuse in images  
## derived from it.  
FROM debian:jessie  
MAINTAINER Paul LaMar <pal3@outlook.com>  
  
# Set language to UTF-8  
ENV LANG C.UTF-8  
# Set TERM to XTERM  
ENV TERM xterm  
  
# Add utility scripts: p_addpkgs, p_adduser  
COPY p_* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/p_*  
  

