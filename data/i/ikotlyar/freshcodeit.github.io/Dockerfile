FROM ruby:2.2  
EXPOSE 4000  
WORKDIR /usr/src/app2  
COPY . /usr/src/app2  
RUN gem install jekyll && gem install jekyll-sitemap  
RUN jekyll build  
CMD jekyll serve --host=0.0.0.0 --watch --incremental

