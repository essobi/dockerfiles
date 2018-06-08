FROM ruby:2-onbuild  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Berlin
/etc/localtime  
  
ENV LANG C.UTF-8  
CMD ["clockwork", "clock.rb"]  

