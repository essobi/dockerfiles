FROM python:3.6  
RUN apt-get update \  
&& apt-get install -y wget python3-tk \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app  
RUN /usr/bin/wget http://otgw.tclcode.com/download/otmonitor-x64 -O
/app/otmonitor  
RUN chmod +x /app/otmonitor  
  
CMD ["/app/otmonitor", "--daemon", "-f", "/app/otmonitor.conf"]

