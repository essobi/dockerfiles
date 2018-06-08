FROM httpd  
ADD . /VisualizationG5/  
WORKDIR /VisualizationG5/  
RUN apt-get update  
RUN apt-get -y install wget git  
RUN wget https://deb.nodesource.com/setup_7.x  
RUN bash setup_7.x  
RUN apt-get install -y nodejs  
RUN apt-get install -y build-essential  
RUN cd react && npm install && npm run build && cd ..  
RUN mkdir /usr/local/apache2/htdocs/widgets  
RUN cp express/react/* /usr/local/apache2/htdocs/widgets  
RUN cp iFrame\ Widget/Dokumentation/* /usr/local/apache2/htdocs/  

