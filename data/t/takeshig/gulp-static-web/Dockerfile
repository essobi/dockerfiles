FROM takeshig/ruby-node  
  
ENV RUBYOPT -Eutf-8  
RUN apt-get update && apt-get install -y --no-install-recommends rsync  
RUN gem install sass compass  
RUN npm install -g gulp bower coffee-script  
  
CMD [ "bash" ]

