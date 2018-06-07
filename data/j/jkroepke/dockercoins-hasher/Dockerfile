FROM ruby  
RUN gem install sinatra  
RUN gem install thin  
ADD hasher.rb /  
CMD ["ruby", "hasher.rb"]  
EXPOSE 8080  
LABEL io.openshift.expose-services "8080:http" io.k8s.display-
name="dockercoins hasher"  

