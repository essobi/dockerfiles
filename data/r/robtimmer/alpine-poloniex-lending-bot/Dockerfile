# Use Alpine Linux based Python 2.7 image as base  
FROM python:2.7-alpine3.6  
# Set maintainer info  
MAINTAINER Rob Timmer <rob@robtimmer.com>  
  
# Set environement variables  
ENV GIT_CHECKOUT_HASH="7d0e3fc390ec21e67aaa2d3155bdac0e1121c149"  
# Install dependencies  
RUN apk add --no-cache --update \  
git build-base  
  
# Set working directory  
WORKDIR /opt/poloniex-lending-bot  
  
# Git clone Poloniex Lending Bot and checkout to the specified hash  
RUN git clone https://github.com/BitBotFactory/poloniexlendingbot . && \  
git checkout $GIT_CHECKOUT_HASH  
  
# Install source code Python dependencies  
RUN pip --no-cache-dir install -r requirements.txt  
  
# Expose required port  
EXPOSE 8000  
# Add volume for configuration file  
VOLUME ["/opt/poloniex-lending-bot/default.cfg"]  
  
# Set entrypoint to source code main script  
ENTRYPOINT ["python", "lendingbot.py"]  

