FROM abernix/meteord:node-8-base  
  
RUN apt-get update  
# make sure the package repository is up to date  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN apt-get update  
RUN apt-get install -y unzip wget curl git  
  
#install redis  
RUN apt-get update && apt-get install -y redis-server  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN wget
http://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip  
RUN unzip chromedriver_linux64.zip  
RUN chmod +x chromedriver  
RUN mv -f chromedriver /usr/local/share/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver  
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver  
  
# Install vnc, xvfb in order to create a 'fake' display and chrome  
RUN apt-get install -y --allow-unauthenticated google-chrome-stable  
RUN apt-get install -y x11vnc xvfb  
  
ENV DISPLAY :99  
# Allow root to execute Google Chrome by replacing launch script  
# ADD google-chrome-launcher /usr/bin/google-chrome  
RUN chmod a+x /usr/bin/google-chrome  
#Add Chrome Renderer  
RUN npm i -g git+https://github.com/afrog33k/chrome-headless-render-pdf.git  
  
# RUN apt-get install wkhtmltopdf xvfb -y  
# RUN echo -e '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24"
/usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh  
# RUN chmod a+x /usr/bin/wkhtmltopdf.sh && rm /usr/local/bin/wkhtmltopdf; exit
0  
# RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

