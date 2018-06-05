FROM homeassistant/home-assistant:latest  
  
ADD https://raw.githubusercontent.com/OpenZWave/open-
zwave/master/config/linear/GC-TBZ48.xml /usr/local/lib/python3.6/site-
packages/python_openzwave/ozw_config/linear/GC-TBZ48.xml  
  
RUN sed -i '/<Manufacturer id="014f" name="Linear">/a <Product type="5442"
id="5436" name="GC-TBZ48 Thermostat" config="linear\/GC-TBZ48.xml"\/>'
/usr/local/lib/python3.6/site-
packages/python_openzwave/ozw_config/manufacturer_specific.xml  
  
CMD [ "python", "-m", "homeassistant", "--config", "/config" ]  

