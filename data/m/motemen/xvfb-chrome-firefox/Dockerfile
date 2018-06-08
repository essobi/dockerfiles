FROM ubuntu  
  
RUN apt-get update && apt-get install -y curl  
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add -  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update && apt-get install -y xvfb firefox google-chrome-stable &&
apt-get clean  

