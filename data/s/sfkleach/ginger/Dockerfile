FROM ubuntu:14.04  
MAINTAINER Stephen Leach "sfkleach@gmail.com"  
ENV REFRESHED_AT 2015-03-15  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make git python3 g++
autoconf uuid-dev libreadline-dev wget libpcap-dev libssl-dev libgmp-dev  
ENV SPICERY_DEV_HOME=/tmp  
ENV GINGER_DEV_HOME=/tmp/ginger  
COPY apps/ /tmp/ginger/apps/  
COPY projects/ /tmp/ginger/projects/  
COPY instruction_set/ /tmp/ginger/instruction_set/  
COPY config* /tmp/ginger/  
COPY devtools/docker-scripts/ /tmp/ginger/devtools/docker-scripts/  
COPY appginger.png /tmp/ginger/  
COPY Makefile.in /tmp/ginger/  
COPY autodocs/ /tmp/ginger/autodocs/  
COPY AUTHORS BUGS NEWS THANKS COPYING /tmp/ginger/  
COPY JumpStart.makefile /tmp/ginger  
WORKDIR /tmp/ginger  
RUN make -f JumpStart.makefile ubuntu  
RUN make -f JumpStart.makefile configure  
RUN make install  
WORKDIR /root  
CMD /usr/local/bin/ginger  

