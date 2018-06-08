FROM alpine:3.7  
# Install dependencies  
RUN apk --no-cache add git postgresql-dev build-base linux-headers libffi
libffi-dev ruby ruby-dev ruby-bundler ruby-irb zlib zlib-dev tzdata  
  
# Add kiosk user and change working directory  
RUN adduser -D kiosk  
WORKDIR /home/kiosk  
  
# Get the code and install dependencies  
RUN git clone https://github.com/kif-ev/oskiosk-server.git && \  
cd oskiosk-server && \  
bundle install --without test development && \  
chown -R kiosk:kiosk /home/kiosk  
  
# Add database config  
ADD database.yml /home/kiosk/oskiosk-server/config/database.yml  
  
# Start script  
USER kiosk  
EXPOSE 8000  
WORKDIR /home/kiosk/oskiosk-server  
CMD sleep 10 && rake db:migrate && unicorn -p 8000 -c ./config/unicorn.rb  

