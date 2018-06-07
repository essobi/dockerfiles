FROM keathley/elixir-node:1.4.2  
  
ENV PHANTOMJS_VERSION=2.1.12  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ENV PYTHONIOENCODING=UTF-8  
  
RUN apt-get install -y \  
python \  
python-dev \  
python-pip  
  
RUN pip install awscli  
  
RUN npm install --quiet -g "phantomjs-prebuilt@$PHANTOMJS_VERSION"  
  
CMD ["bin/bash"]  

