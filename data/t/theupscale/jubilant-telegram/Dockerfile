FROM node:5-onbuild  
MAINTAINER Saransh Sharma <saransh@theupscale.in>, Upscale Team
<team@theupscale.in>  
  
  
RUN git clone https://github.com/maektwain/jubilant-telegram app  
  
RUN node -v  
  
RUN cd app && ls && npm install  
  
ADD run.sh app/run.sh  
RUN chmod +x app/run.sh  
  
COPY .env app/  
  
EXPOSE 4000  
CMD ["start"]  
  
ENTRYPOINT ["app/run.sh"]  

