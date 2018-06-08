FROM xblaster/generic_node  
  
RUN git clone https://github.com/xblaster/quickCooking3-UI  
WORKDIR quickCooking3-UI  
RUN npm install  
RUN git pull\  
&& bower install --allow-root  
  
RUN git pull  
  
EXPOSE 9000  
CMD grunt serve:dist  

