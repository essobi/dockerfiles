FROM centos:6  
ENV LD_LIBRARY_PATH=/usr/local/python3.5/lib  
ENV PATH=/usr/local/python3.5/bin:$PATH  
  
ADD https://github.com/srault95/python-
binary/releases/download/0.2.0/python3.5-x86-64.tar.gz /tmp/  
  
RUN tar -xzf /tmp/python3.5-x86-64.tar.gz -C / \  
&& rm -f /tmp/python3.5-x86-64.tar.gz \  
&& pip install pyinstaller  
  
CMD "pyinstaller"  

