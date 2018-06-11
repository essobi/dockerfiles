FROM dockerfile/java  
MAINTAINER Daekwon Kim <propellerheaven@gmail.com>  
  
# Run apt-get update  
RUN apt-get update && apt-get -y upgrade  
  
# Inastll Play framework  
WORKDIR /root  
RUN curl -O http://downloads.typesafe.com/play/2.1.0/play-2.1.0.zip  
RUN unzip play-2.1.0.zip  
RUN mv play-2.1.0 play  
  
# Clone Yobi  
RUN git clone https://github.com/nforge/yobi.git /root/play/yobi  
RUN cd /root/play/yobi;../play compile  
  
# Run Yobi  
EXPOSE 9000  
ADD ./start.sh /root/play/yobi/  
RUN chmod +x /root/play/yobi/start.sh  
WORKDIR /root/play/yobi  
CMD /bin/bash -c ./start.sh  

