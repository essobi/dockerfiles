FROM debian:sid  
  
ADD cd-bare /cd-bare  
  
RUN apt-get update && \  
apt-get -y install libglib2.0 libnss3-dev libxtst6 libxss1 libgconf-2-4
libfontconfig1 libpango1.0-0 libxcursor1 libxcomposite1 libasound2 libxdamage1
libxrandr2 libcups2 libgtk-3-0 wget unzip xvfb fonts-noto fonts-liberation
libexif12 pulseaudio && \  
rm -rf /var/lib/apt/lists/* && \  
gpasswd -a root pulse-access  
  
RUN ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-
gnu/libudev.so.0  
  
RUN wget -O chromium.zip https://download-chromium.appspot.com/dl/Linux_x64 &&
\  
unzip chromium.zip && \  
mv chrome-linux/chrome_sandbox chrome-linux/chrome-sandbox && \  
chown root.root chrome-linux/chrome-sandbox && \  
chmod 4755 chrome-linux/chrome-sandbox && \  
rm chromium.zip  
  
RUN wget -O /tmp/chromedriver-version
http://chromedriver.storage.googleapis.com/LATEST_RELEASE && \  
wget http://chromedriver.storage.googleapis.com/`cat /tmp/chromedriver-
version`/chromedriver_linux64.zip && \  
unzip chromedriver_linux64.zip && \  
rm chromedriver_linux64.zip /tmp/chromedriver-version  
  
RUN wget https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-
hinted.zip && \  
unzip NotoSansCJKjp-hinted.zip && \  
mkdir -p usr/share/fonts/truetype/noto && \  
mv *.otf usr/share/fonts/truetype/noto/ && \  
fc-cache && \  
rm NotoSansCJKjp-hinted.zip  
  
RUN sed -i 's/"$@"/"$@" --no-sandbox/' chrome-linux/chrome-wrapper && \  
ln -s /chrome-linux/chrome-wrapper /usr/bin/google-chrome  
  
RUN echo "#!/bin/bash" > /cd && \  
echo 'exec /cd-bare --whitelisted-ips 0.0.0.0/0' >> /cd && \  
chmod u+x /cd  
  
CMD ["/cd"]  

