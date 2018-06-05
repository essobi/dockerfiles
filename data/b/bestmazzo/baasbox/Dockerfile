FROM java:8  
MAINTAINER Matteo Mazzoni <matteo@bestmazzo.it>  
WORKDIR /baasbox  
  
# 0.9.5  
RUN wget --content-disposition
"http://opensource.baasbox.com/?wpdmact=process&did=NTUuaG90bGluaw=="  
RUN unzip baasbox*.zip  
RUN rm baasbox*.zip  
RUN mv baasbox-*/ baasbox/  
RUN chmod +x baasbox/start  
  
VOLUME /baasbox/db  
EXPOSE 9000  
ENTRYPOINT ["bash","baasbox/start"]  
  

