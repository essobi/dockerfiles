FROM ubuntu:16.04  
RUN apt-get update && apt-get dist-upgrade -yq && apt-get install -yq
software-properties-common  
  
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release
-sc) universe multiverse" && add-apt-repository "deb
http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc)-updates universe
multiverse"  
  
RUN apt-get update && apt-get install -yq sudo nano wget htop git  
  
RUN mkdir /generator && cd /generator && git clone
https://github.com/forknote/cryptonote-generator.git . && /bin/bash
./install_dependencies.sh  
  
VOLUME ["/config"]  
VOLUME ["/generator/generated_files"]  
  
WORKDIR /generator  
  
ENTRYPOINT ["/bin/bash", "generator.sh"]  
CMD ["-f", "config_example.json"]  

