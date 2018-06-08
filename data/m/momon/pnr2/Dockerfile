FROM beevelop/nodejs-python  
  
MAINTAINER anon <anon@anon.me>  
  
RUN apt-get update && apt-get install -y ruby-full wget nano curl && \  
pip install livestreamer && \  
npm install -g request minimist && \  
gem install httparty sys-proctable eventmachine em-http-request --no-rdoc
--no-ri && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
WORKDIR /app  
COPY app/* ./  
RUN npm link request minimist  
CMD ruby main.rb  

