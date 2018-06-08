FROM debian:jessie  
MAINTAINER YAMADA Tsuyoshi <tyamada@minimum2scp.org>  
RUN apt-get update && apt-get install -y --no-install-recommends stress &&
apt-get clean  
ENTRYPOINT [ "/usr/bin/stress" ]  

