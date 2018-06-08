# meedan/chrome  
# meedan/nodejs + and npm chrome-remote-interface minimist  
FROM meedan/ruby  
  
# chrome repo  
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google.list  
  
# install stuff needed to take screenshots  
RUN npm install -g chrome-remote-interface minimist  
RUN apt-get update && apt-get install -y --no-install-recommends \  
google-chrome-stable  

