FROM alpine:3.2  
MAINTAINER James Mills, prologic at shortcircuit dot net dot au  
  
CMD ["python"]  
  
RUN \  
apk add --update ca-certificates python && \  
rm -rf /var/cache/apk/* && \  
python -c 'from urllib import urlretrieve;
urlretrieve("https://bootstrap.pypa.io/ez_setup.py", "ez_setup.py")' && python
ez_setup.py && rm ez_setup.py && \  
python -c 'from urllib import urlretrieve;
urlretrieve("https://bootstrap.pypa.io/get-pip.py", "ez_setup.py")' && python
ez_setup.py && rm ez_setup.py && \  
rm /*.zip && \  
rm -rf /root/.cache && \  
rm -rf $(find /usr/lib/python2.7 -type d -name "test*") && \  
rm -rf /usr/lib/python2.7/ensurepip && \  
rm -rf /usr/lib/python2.7/idlelib && \  
rm -rf /usr/lib/python2.7/lib2to3 && \  
rm -rf /usr/lib/python2.7/lib-tk && \  
rm /usr/bin/idle && \  
python -m compileall /usr/lib/python2.7 && \  
rm $(find /usr/lib/python2.7 -type f -name "*.py") && \  
rm $(find /usr/lib/python2.7 -type f -name "*.pyo")  

