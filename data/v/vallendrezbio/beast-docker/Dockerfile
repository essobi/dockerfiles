FROM java:8-jre  
  
LABEL maintainer="vallardt@gmail.com"  
  
ENV BEAST_VERSION 1.8.4  
RUN wget https://github.com/beast-dev/beast-
mcmc/releases/download/v${BEAST_VERSION}/BEASTv${BEAST_VERSION}.tgz -O- | \  
tar xzvf -  
RUN mv BEASTv${BEAST_VERSION}/bin/* /usr/local/bin/  
RUN mv BEASTv${BEAST_VERSION}/lib/* /usr/local/lib/  
  
RUN groupadd -r developer -g 1000 && useradd -r -u 1000 -g developer -G
audio,video developer  
RUN mkdir -p /home/developer && chown -R developer:developer /home/developer  
  
WORKDIR /home/developer  
USER developer  

