FROM alpine:latest  
  
# NOTE: pip is installed with python3 in alpine repos.  
  
RUN apk add --update --no-cache python3 && \  
find / -type d -name __pycache__ -exec rm -r {} + && \  
rm -r /usr/lib/python*/ensurepip && \  
rm -r /usr/lib/python*/lib2to3 && \  
rm -r /usr/lib/python*/turtledemo && \  
rm -r /usr/lib/python*/idlelib && \  
rm /usr/lib/python*/turtle.py && \  
rm /usr/lib/python*/webbrowser.py && \  
rm /usr/lib/python*/doctest.py && \  
rm /usr/lib/python*/pydoc.py && \  
rm -rf /root/.cache /var/cache /usr/share/terminfo  

