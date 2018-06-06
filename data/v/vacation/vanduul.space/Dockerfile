FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
git curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN git clone https://github.com/jason-weirather/vanduul.space.git \  
&& cd vanduul.space && npm install \  
&& npm run build  
RUN npm install -g http-server  
WORKDIR /vanduul.space/build/  
CMD ["http-server", "-s"]

