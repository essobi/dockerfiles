FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y python  
RUN mkdir /site  
WORKDIR /site  
RUN touch index.html  
EXPOSE 8000  
RUN echo '<h1>Hello World</h1>' >> index.html  
CMD "python" "-m" "SimpleHTTPServer"  

