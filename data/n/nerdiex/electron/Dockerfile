FROM nerdiex/node:latest  
MAINTAINER Muhammad Sayuti "muhammad.sayuti94@gmail.com"  
  
RUN apt-get install -y \  
libgtk2.0-dev \  
libxtst-dev \  
libxss1 \  
libgconf2-dev \  
libnss3-dev \  
libasound2-dev \  
xvfb \  
xfonts-75dpi \  
xfonts-base \  
gnupg \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libpulse0 \  
libv4l-0 \  
fonts-symbola --no-install-recommends  
# install global node modules  
RUN yarn global add electron typescript tslint ts-node  
  
WORKDIR /projects  

