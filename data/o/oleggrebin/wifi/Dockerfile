FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y --fix-missing wget git firefox python
python-pip xvfb xserver-xephyr vnc4server  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz  
RUN tar -xvzf geckodriver* && chmod +x geckodriver && mv geckodriver /bin/ &&
export PATH=$PATH:/bin/geckodriver  
RUN pip install selenium requests pyvirtualdisplay  
RUN git clone \--depth 1 https://oleggrebin@bitbucket.org/oleggrebin/wifi.git  
RUN cd wifi && mv main.py ../ && mv id ../ && mv node ../  
RUN python main.py

