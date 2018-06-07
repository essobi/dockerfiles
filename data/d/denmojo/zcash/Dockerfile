FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y --no-install-recommends apt-
transport-https ca-certificates wget  
  
RUN wget -O - https://apt.z.cash/zcash.asc | apt-key add -  
  
RUN echo "deb https://apt.z.cash/ jessie main" | tee
/etc/apt/sources.list.d/zcash.list  
  
RUN apt-get update && apt-get install -y zcash  
  
RUN zcash-fetch-params  
  
CMD zcashd  
  
# docker build -t zcash  
## e.g. in macOS:  
## create a directory: ~/.zcash  
## in that directory, touch zcash.conf  
## add in there any configurations such as gen=1 to enable CPU mining  
# docker run -v /Users/<whoever>/.zcash:/root/.zcash --name zcashd --rm -ti
zcash  

