FROM cocoon/restop  
  
ENV PYTHONPATH=/usr/local/lib/restop  
  
WORKDIR /app/restop-devices  
ADD requirements.txt .  
RUN /env/bin/pip install -r requirements.txt  
  
WORKDIR /usr/local/lib  
  
# install restop-devices  
RUN git clone https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/restop-
devices.git \  
&& mv restop-devices/restop_components restop/ \  
&& mv restop-devices/droydrunner restop/ \  
&& mv restop-devices/tvboxrunner restop/ \  
&& mv restop-devices/bstvboxrunner restop/ \  
&& mv restop-devices/tvstickrunner restop/ \  
&& mv restop-devices/tvstickappdriver restop/ \  
&& mv restop-devices/liveboxrunner restop/ \  
&& mv restop-devices/sliveboxrunner restop/ \  
&& mv restop-devices/tvphoenixrunner restop/ \  
&& mv restop-devices/doc restop/ \  
&& mv restop-devices/tvbox_components restop/  
  
# install restop-ide  
RUN git clone
https://cocoon_bitbucket@bitbucket.org/orangeparis/restop_blockly.git \  
&& mv restop_blockly/restop_ide/ restop/  
  
CMD ["ash"]

