FROM ruby  
RUN apt-get -y update && apt-get -y install libicu-dev  
RUN gem install gollum  
RUN gem install redcarpet org-ruby  
VOLUME /wiki  
WORKDIR /wiki  
CMD ["gollum", "--port", "80", "--live-preview", "--h1-title", "--allow-
uploads", "page", "--css"]  
EXPOSE 80  

