FROM nginx  
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
COPY nginx/chess.conf /etc/nginx/chess.conf  
RUN ls /etc/nginx  
RUN mkdir /static  
COPY app/static/ /static

