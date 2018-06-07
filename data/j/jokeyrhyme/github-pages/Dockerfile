FROM ruby  
  
MAINTAINER Ron Waldon <jokeyrhyme@gmail.com>  
  
RUN gem install --no-document github-pages -v 20  
  
VOLUME ['/usr/app/src']  
WORKDIR /usr/app/src  
  
EXPOSE 4000  
CMD jekyll serve --watch --drafts --baseurl ''  

