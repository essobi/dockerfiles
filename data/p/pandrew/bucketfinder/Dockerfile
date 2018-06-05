FROM ruby:2.3.1-alpine  
  
RUN apk --no-cache add curl \  
&& curl -fL https://digi.ninja/files/bucket_finder_1.1.tar.bz2 >
bucket_finder.bz2 \  
&& tar -jxvf bucket_finder.bz2 \  
&& rm -fv bucket_finder.bz2  
  
WORKDIR bucket_finder  
ENTRYPOINT ["./bucket_finder.rb"]  

