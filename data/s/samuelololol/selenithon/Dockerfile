FROM samuelololol/docker-selenium  
MAINTAINER samuelololol <samuelololol@gmail.com>  
ENV VER=v0.19.1  
#VER=$(wget -O - https://github.com/mozilla/geckodriver/releases/latest
2>/dev/null | grep "Release v" | awk -F "Release v" '{print $2}' | awk -F " "
'{print $1}'); \  
#VER=$(curl -sL \\\n
https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep
tag_name | cut -d '"' -f 4'"')  
USER root  
RUN mkdir -p /app  
WORKDIR /app  
RUN apt-get update  
RUN apt-get install -y python-dev python-pip python-sklearn \  
libgtk-3-0 libgtk-3-common libdbus-glib-1-dev dbus-x11 xvfb \  
python-pyaudio sox portaudio19-dev libatlas-base-dev \  
postgresql postgresql-contrib libpq-dev  
RUN pip install --upgrade pip  
RUN pip install xvfbwrapper pyvirtualdisplay\  
selenium selenium-requests six requests\  
virtualenv virtualenvwrapper \  
lxml BeautifulSoup \  
pyaudio matplotlib numpy scipy \  
pytest  
RUN cd /app; \  
LINK_PREFIX="https://github.com/mozilla/geckodriver/releases/download"; \  
wget $LINK_PREFIX"/"$VER"/geckodriver-"$VER"-linux64.tar.gz"  
RUN cd /app; \  
tar zxf geckodriver*; \  
chmod +x geckodriver; chown root.root geckodriver; mv geckodriver
/usr/local/bin; \  
rm -rf /app/*  
RUN apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /var/lib/apt-lists/*  
ENTRYPOINT ["/entry_point.sh"]  
WORKDIR /app  
CMD ["--version"]  
ADD entry_point.sh /entry_point.sh  

