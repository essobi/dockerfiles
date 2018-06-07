FROM monster1025/alpine86-python  
  
ENV LIBRARY_PATH=/lib:/usr/lib  
RUN pip install --upgrade pip && pip install homeassistant  
  
EXPOSE 8123  
CMD ["/usr/bin/hass"]  

