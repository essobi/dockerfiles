FROM node:8  
LABEL maintainer="Virgilio Missão Neto <virgilio.missao.neto@gmail.com>"  
RUN apt-get update \  
&& apt-get install -y xvfb \  
libnotify4 \  
libgconf2-4 \  
libnss3 \  
libxtst-dev \  
libc6 \  
libstdc++6 \  
libgcc1 \  
libgtk2.0-0 \  
libasound2 \  
libxrender1 \  
libxss1  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
RUN yarn global add electron@1.8.1  
  
CMD xvfb-run -a --server-args='-screen 0, 1280x800x24' electron .  

