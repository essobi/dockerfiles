# BUILD-USING: docker build -t nerve-registry .  
# PUSH-USING: docker tag nerve-registry surf/nerve-registry && docker push
surf/nerve-registry  
FROM surf/base-ruby  
  
# add the application and bundle  
ADD . /app  
WORKDIR /app  
RUN bundle install --deployment  
  
ENV NERVE_CONFIG /app/config.json  
CMD ["/app/run.sh"]  

