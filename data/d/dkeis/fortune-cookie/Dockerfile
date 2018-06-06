FROM python:3.4  
RUN apt-get update && \  
apt-get install -y libsasl2-2 libsvn1 libpython2.7 python2.7 && \  
ln -s libsasl2.so.2.0.25 /usr/lib/x86_64-linux-gnu/libsasl2.so.3 && \  
ln -s libsvn_delta-1.so.1.0.0 /usr/lib/x86_64-linux-gnu/libsvn_delta-1.so.0 &&
\  
ln -s libsvn_subr-1.so.1.0.0 /usr/lib/x86_64-linux-gnu/libsvn_subr-1.so.0 && \  
rm -rf /var/lib/apt/lists/*  
COPY requirements.txt /requirements.txt  
RUN pip install -r requirements.txt  
COPY cookie.py cookie.sh /  
CMD /cookie.sh  

