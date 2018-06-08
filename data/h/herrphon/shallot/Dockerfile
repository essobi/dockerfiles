FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y build-essential \  
git \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app \  
&& cd /app \  
&& git clone https://github.com/apk/katmagic.git \  
&& cd katmagic \  
&& ./configure \  
&& make \  
&& cp shallot /usr/bin \  
&& cd / \  
&& rm -rf /app  
  
CMD ["shallot", "^test"]  
  

