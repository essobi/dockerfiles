FROM node:latest  
  
# Install google chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub >
/linux_signing_key.pub  
RUN apt-key add /linux_signing_key.pub  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update  
RUN apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 google-chrome-
stable  
  
# Install lighthouse  
RUN npm install -g lighthouse  
  
# Install chromedriver  
RUN wget -N
http://chromedriver.storage.googleapis.com/2.34/chromedriver_linux64.zip -P ~/
&& \  
unzip ~/chromedriver_linux64.zip -d ~/ && \  
rm ~/chromedriver_linux64.zip && \  
mv -f ~/chromedriver /usr/local/bin/chromedriver && \  
chown root:root /usr/local/bin/chromedriver && \  
chmod 0755 /usr/local/bin/chromedriver  
  
# Create a chrome user  
RUN groupadd -r chromeuser  
RUN useradd -r -g chromeuser -G audio,video chromeuser  
RUN mkdir -p /home/chromeuser  
RUN chown -R chromeuser:chromeuser /home/chromeuser  
USER chromeuser  
  
VOLUME /home/chromeuser  
WORKDIR /home/chromeuser  
  
CMD ["/bin/bash"]  

