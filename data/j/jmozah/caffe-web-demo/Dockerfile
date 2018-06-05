# Don't edit this file directly, since it was generated from a template,  
# and you're changes will be *clobbered*. Edit the template instead.  
FROM tleyden5iwx/caffe  
  
# Install python deps for web-app  
RUN cd /opt/caffe/examples/web_demo && \  
(pip install -r requirements.txt)  
  
RUN bash -c 'echo "export PYTHONPATH=/opt/caffe/python:\$PYTHONPATH" >>
~/.bashrc'  

