FROM ruby:2.3-alpine  
LABEL maintainer="Tobias L. Maier <tobias.maier@baucloud.com>"  
  
RUN echo 'gem: --no-document' >> /etc/gemrc  
  
RUN gem install gemfury  
  
WORKDIR /workdir  
  
ENTRYPOINT ["fury"]  
CMD ["--help"]  

