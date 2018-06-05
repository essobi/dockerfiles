FROM ubuntu:latest  
LABEL maintainer "ripples <w@q2zy.com>"  
  
RUN apt-get update && apt-get install -y \  
sudo \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd ~/ \  
&& wget -qO-
https://github.com/BinaryAnalysisPlatform/qira/archive/v1.2.tar.gz | tar zx \  
&& cd qira-1.2 \  
&& yes | ./install.sh \  
&& ./fetchlibs.sh  
  
EXPOSE 3002  
EXPOSE 4000  
ENTRYPOINT ["qira"]  

