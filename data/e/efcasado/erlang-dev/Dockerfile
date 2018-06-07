###========================================================================  
### File: Dockerfile  
###  
### TBD  
###  
### Author(s):  
### - Enrique Fernandez <enrique.fernandez@erlang-solutions.com>  
###========================================================================  
FROM erlang:18.2-slim  
  
# Install Git  
RUN apt-get update && \  
apt-get install -y \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install rebar3  
RUN git clone -b beta-4 https://github.com/rebar/rebar3/ /opt/rebar3 && \  
cd /opt/rebar3 && \  
./bootstrap && \  
chmod a+x rebar3 && \  
mv rebar3 /usr/bin/ && \  
cd / && \  
rm -rf /opt/rebar3  

