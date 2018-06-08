FROM needleops/consul  
  
COPY pip.conf /root/.config/pip/  
RUN curl -Ls https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py \  
&& apk add -U python3 \  
&& python3 /tmp/get-pip.py \  
&& pip install virtualenv \  
&& virtualenv -p /usr/bin/python3 /env \  
&& /env/bin/pip install setuptools \--upgrade \  
&& rm /tmp/get-pip.py /var/cache/apk/*  
  
ENV TERM "xterm"  
WORKDIR /app  
  
CMD ["/env/bin/python"]  

