FROM apluslms/grading-python:3.5-1.1  
ENV LANG C.UTF-8  
RUN apt-get update -qqy && apt-get install -qqy --no-install-recommends \  
wbritish \  
xvfb \  
xauth \  
&& echo "deb http://archive.ubuntu.com/ubuntu precise universe restricted" >>
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu precise-security main universe
restricted" >> /etc/apt/sources.list \  
&& apt-get update -qqy && apt-get install -qqy --no-install-recommends
--allow-unauthenticated \  
firefox \  
&& head -n -2 /etc/apt/sources.list > tmp.list \  
&& mv tmp.list /etc/apt/sources.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN curl -SLO
https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
\  
&& tar zxvf geckodriver-v0.17.0-linux64.tar.gz \  
&& mv geckodriver /usr/local/bin/ \  
&& rm geckodriver-v0.17.0-linux64.tar.gz  
  
ADD requirements.txt /root  
RUN pip3 install -r /root/requirements.txt \  
&& rm -rf /root/.cache  
  
ADD bin /usr/local/bin  
ADD assets /assets  

