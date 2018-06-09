FROM tutum/apache-php  
RUN rm -rf /app  
ADD . /app  
ENV ALLOW_OVERRIDE true  
ENV HOSTNAME ${hostname:-HOSTNAME}  
ENV USERNAME ${username:-USERNAME}  
ENV PASSWORD ${password:-PASSWORD}  
ENV DATABASE ${database:-DATABASE}  
EXPOSE 80

