FROM nmqanh/geekpress:latest  
  
MAINTAINER Nguyen, Manh Quoc Anh <nmqanh@gmail.com>  
  
ADD . /blog/  
WORKDIR /app  
  
ENV BLOG_PATH=/blog  
ENV MIX_ENV prod  
ENV PORT 80  
EXPOSE 80  
RUN npm run link-blog  
RUN mix do compile  
RUN mix phoenix.digest  
  
CMD ["mix","phoenix.server"]  

