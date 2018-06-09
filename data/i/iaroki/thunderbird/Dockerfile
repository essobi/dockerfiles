FROM debian:stretch  
MAINTAINER iaroki  
RUN apt-get update -y && apt-get install fonts-droid-fallback thunderbird -y
&& apt-get clean  
RUN adduser iaroki  
USER iaroki  
CMD ["thunderbird"]  

