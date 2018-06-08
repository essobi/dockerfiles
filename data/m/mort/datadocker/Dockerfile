# Docker container for imagery and course data  
FROM debian:jessie  
MAINTAINER Mort Canty "mort.canty@gmail.com"  
ENV REFRESHED_AT 2016-03-31.  
RUN mkdir -p /home/imagery  
COPY imagery /home/imagery  
COPY figures /home/imagery/figures  
COPY ZFL-Course-Part1.ipynb /home/imagery/ZFL-Course-Part1.ipynb  
COPY ZFL-Course-Part2.ipynb /home/imagery/ZFL-Course-Part2.ipynb  
COPY ZFL-Course-Part3.ipynb /home/imagery/ZFL-Course-Part3.ipynb  
COPY ZFL-Course-Part4.ipynb /home/imagery/ZFL-Course-Part4.ipynb  
COPY pca.ipynb /home/imagery/pca.ipynb  
RUN chmod -R u+x /home/imagery/figures  
VOLUME /home/imagery

