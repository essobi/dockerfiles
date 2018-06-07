FROM ampush/base-pyservice:v5  
  
RUN pip3 install --upgrade pip  
  
# Set the project name  
ENV PROJECT_NAME="kraken"  
# Copy over the source  
RUN mkdir -p /code/$PROJECT_NAME  
  
WORKDIR /code/$PROJECT_NAME  
  
ADD ./requirements.txt /code/$PROJECT_NAME/requirements.txt  
  
# Install the requirements.txt  
RUN yes | pip3 install -r requirements.txt  
  
# ADD the app#  
ADD . /code/$PROJECT_NAME  
  
ADD config /config/  
  
# Exposing your app port  
EXPOSE 80  
# We need wget to set up the PPA and xvfb to have a virtual screen and unzip
to install the Chromedriver  
RUN apt-get -qq update  
RUN apt-get -qq -y install wget xvfb unzip  
  
# Set up the Chrome PPA  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
  
# Update the package list and install chrome  
RUN apt-get update -y  
RUN apt-get install -y google-chrome-stable  
  
# Set up Chromedriver Environment variables  
ENV CHROMEDRIVER_VERSION 2.36  
ENV CHROMEDRIVER_DIR /chromedriver  
RUN mkdir $CHROMEDRIVER_DIR  
  
# Download and install Chromedriver  
RUN wget -q --continue -P $CHROMEDRIVER_DIR
"http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"  
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR  
  
# Put Chromedriver into the PATH  
ENV PATH $CHROMEDRIVER_DIR:$PATH  
  
RUN mv $CHROMEDRIVER_DIR/chromedriver /usr/local/bin  
  
RUN chmod a+x /usr/local/bin/chromedriver  
  
#enable the browser display and in case we need to take screenshots  
RUN Xvfb :99 -ac -screen 0 1280x1024x24 &  
RUN nice -n 10 x11vnc 2>&1 &  
  
CMD ["/usr/local/bin/dumb-init", "/usr/local/bin/start.sh"]  

