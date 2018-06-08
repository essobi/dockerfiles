FROM ruby  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN git clone https://github.com/github/markup \  
&& cd markup \  
&& bundle install  
  
WORKDIR /work  
  
ENTRYPOINT ["github-markup"]  
CMD ["--help"]  

