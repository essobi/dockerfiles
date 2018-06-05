FROM ubuntu:16.10  
USER root  
  
RUN apt-get update  
  
RUN apt-get install -y curl sudo  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
  
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list'  
  
RUN apt-get update  
  
RUN apt-get install -y build-essential git google-chrome-unstable nodejs  
  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
ENV CHROME_BIN /usr/bin/google-chrome-unstable  
  
RUN npm install -g @angular/cli@latest  

