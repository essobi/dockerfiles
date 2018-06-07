FROM debian  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
git \  
libasound2-dev \  
curl \  
automake \  
make \  
nano \  
g++ \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/wb2osz/direwolf.git  
WORKDIR /direwolf  
RUN make  
RUN make install  
RUN make install-conf  
  
VOLUME /direwolf  
WORKDIR /direwolf  
  
CMD direwolf  

