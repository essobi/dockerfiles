FROM watsy0007/rails_gems:5.0.0.1  
RUN apt-get update && \  
apt-get install nodejs -y && \  
apt-get install npm -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
COPY Gemfile /tmp  
RUN bundle install  
  
EXPOSE 80  
CMD ["bash"]  

