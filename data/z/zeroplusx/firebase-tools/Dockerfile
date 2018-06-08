FROM zeroplusx/yarn  
  
LABEL vendor="0+X"  
LABEL maintainer="Sebastian Mandrean <sebastian@0x.se>"  
  
WORKDIR /app  
  
# Install dependencies  
RUN yarn global add firebase-tools  
  
ENTRYPOINT ["/usr/local/bin/firebase"]  

