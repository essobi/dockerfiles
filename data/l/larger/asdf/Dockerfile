FROM ubuntu:16.04  
RUN useradd -r -m -U ubuntu \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y git curl build-essential python2.7 sudo \  
&& echo 'ubuntu ALL=NOPASSWD: ALL' >> /etc/sudoers \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean  
  
USER ubuntu  
WORKDIR /home/ubuntu  
ENV PATH /home/ubuntu/.c9/bin:/home/ubuntu/.c9/node/bin:${PATH}  
  
RUN mkdir workspace \  
&& git clone https://github.com/c9/core.git c9sdk \  
&& cd c9sdk \  
&& ./scripts/install-sdk.sh \  
&& npm install -g forever \  
&& npm cache clean  
  
VOLUME /home/ubuntu/workspace  
EXPOSE 8181  
ENTRYPOINT ["forever", "/home/ubuntu/c9sdk/server.js", "-w",
"/home/ubuntu/workspace", "--listen", "0.0.0.0"]  
  
#CMD["--auth","username:password"]

