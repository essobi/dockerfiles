FROM java:8-jdk  
  
# Create a default user  
RUN useradd driven --shell /bin/bash --create-home  
  
# Download dependencies for Pillow, python and selenium, chrome  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y libappindicator1 libxss1 libpango1.0-0 xdg-utils fonts-
liberation libexif12 \  
&& apt-get install -y libjpeg62-turbo-dev zlib1g-dev libtiff5-dev
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev python-tk \  
&& apt-get install -y python-dev python-setuptools xvfb nginx supervisor
python-pip \  
&& apt-get install -y libgtk-3-0 lsb-release \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download cron  
RUN apt-get update && apt-get -y install cron  
  
# Set up locale  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Get google chrome  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome-stable_current_amd64.deb \  
&& rm google-chrome-stable_current_amd64.deb  
  
# Download and add chromedriver to PATH  
RUN apt-get install unzip;  
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip &&
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/  
  
COPY . /driven_api  
WORKDIR /driven_api  
  
ENV DISPLAY :0  
ENV DRIVEN_PYTHON_API_ENV live  
RUN service nginx stop  
RUN pip install -r requirements.txt  
  
# Set up configuration files  
COPY ./supervisord.conf /etc/supervisord.conf  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
# Make sure crontab file exists in current directory  
ADD crontab /etc/cron.d/driven-cron  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/driven-cron  
  
# Create the log file  
RUN touch /var/log/cron.log  
  
EXPOSE 80  
# start supervisor to run our wsgi server  
CMD ["supervisord", "-n"]

