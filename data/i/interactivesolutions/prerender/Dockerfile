FROM node:latest  
  
# Add required external dependencies  
RUN echo deb http://ftp.debian.org/debian/ jessie main contrib non-free >
/etc/apt/source.list  
  
# Install required dependencies  
RUN apt-get update -y && apt-get install -y \  
python2.7 \  
python-pip \  
libfreetype6 \  
libfontconfig \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends \  
&& apt-get clean  
  
# Add a user to run prerender and launch chrome with  
RUN groupadd -r prerender && useradd -r -g prerender -G audio,video prerender
\  
&& mkdir -p /home/prerender && chown -R prerender:prerender /home/prerender  
  
# Change user to avoid permission errors  
USER prerender  
WORKDIR /home/prerender  
  
# Install prerender  
RUN git clone https://github.com/prerender/prerender.git  
  
# Install dependencies  
RUN cd prerender && npm install;  
  
# Incase we want to link something  
EXPOSE 3000  
# Default command  
CMD ["node", "prerender/server.js"]  

