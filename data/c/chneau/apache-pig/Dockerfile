FROM java:7-jre-alpine  
  
ENV PIG_VERSION=0.17.0  
ENV PATH=$PATH:/pig-$PIG_VERSION/bin  
  
RUN apk add --no-cache curl bash \  
&& curl http://apache.cs.utah.edu/pig/pig-$PIG_VERSION/pig-$PIG_VERSION.tar.gz
\  
| tar xzf -  
  
WORKDIR /code  

