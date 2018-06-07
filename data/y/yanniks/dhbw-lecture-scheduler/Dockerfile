FROM node  
  
COPY . /dhbw/  
RUN mkdir /dhbw/tmp && \  
chmod +x /dhbw/dhbw-run && \  
bash -c "cd /dhbw && npm install && npm run build"  
  
EXPOSE 3000  
CMD ["/dhbw/dhbw-run"]  

