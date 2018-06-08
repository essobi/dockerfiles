FROM ruby:2.2.3-onbuild  
ENV PORT 80  
EXPOSE 80  
ENV RACK_ENV production  
ENV PRICING_SERVICE_BASE_URL http://pricing/  
  
CMD ["puma", "-C", "puma.rb"]  

