FROM node:8.6  
MAINTAINER Mirko Akov  
  
# Install Chrome  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update -yqqq && \  
apt-get install -y google-chrome-stable > /dev/null 2>&1 && \  
sed -i 's/"$@"/--no-sandbox "$@"/g' /opt/google/chrome/google-chrome  
  
# Install yarn  
RUN \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
export PATH=$HOME/.yarn/bin:$PATH  
  
# Install bower  
RUN \  
npm install -g bower  

