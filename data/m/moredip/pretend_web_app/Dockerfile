FROM ruby:2.2.3-onbuild  
ENV PORT 80  
EXPOSE 80  
ENV RACK_ENV production  
ENV DEALS_SERVICE_BASE_URL http://deals/  
ENV CATALOG_SERVICE_BASE_URL http://catalog/  
  
CMD ["puma", "-C", "puma.rb"]  

