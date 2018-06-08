FROM homeassistant/home-assistant:0.70.0  
# remove existing python  
RUN pip3 uninstall -y python_openzwave  
  
# install new (dev) version of python_openzwave  
RUN pip3 install --no-cache-dir 'python_openzwave==0.4.4' \--install-option="
--flavor=ozwdev"  
  
# replace component requirement 0.4.3 with 0.4.4  
RUN sed -i 's/0.4.3/0.4.4/'
/usr/src/app/homeassistant/components/zwave/__init__.py  

