# Two stage Dockerfile  
# STAGE 0: Use alpine to get the latest release.  
FROM ubuntu:latest AS build  
RUN apt-get update  
RUN apt-get install -y wget netcat  
# Manually update this  
ENV
PRISM_SOURCE="https://github.com/stoplightio/prism/releases/download/v2.0.0-beta.2/prism_linux_amd64"  
RUN wget -O /prism "${PRISM_SOURCE}"  
CMD ["/bin/bash"]  
  
# STAGE 1: build the ubuntu image with the prism executable downloaded in
STAGE 0  
FROM ubuntu:latest  
COPY \--from=build /prism /usr/bin/prism  
COPY \--from=build /bin/nc /bin/nc  
COPY \--from=build /bin/nc /bin/nc  
COPY \--from=build /usr/bin/wget /usr/bin/wget  
RUN chmod a+x /usr/bin/prism  
ENTRYPOINT ["/usr/bin/prism"]  

