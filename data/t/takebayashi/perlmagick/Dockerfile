FROM perl:5.20.1  
MAINTAINER Shun Takebayashi <shun@takebayashi.asia>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN ln -s /usr/include/x86_64-linux-gnu/ImageMagick-6/
/usr/local/include/ImageMagick-6  
RUN ln -s /usr/lib/x86_64-linux-gnu/libperl.so.5.20.1
/usr/local/lib/libperl.so  
RUN cpanm --notest Image::Magick  
  
CMD ["perl5.20.1","-de0"]  

