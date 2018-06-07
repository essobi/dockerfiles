#Use a Jekykll image with nginx as a parent image  
FROM jekyll/builder  
  
# Set the working directory to /app  
#WORKDIR /tmp/jekyll-site  
WORKDIR /srv/jekyll  
#RUN mkdir /root/.ssh  
# Copy the current directory contents into the container at /app  
# ADD . /tmp/jekyll-site  
ADD . /srv/jekyll/  
  
ENV LANGUAGE "en_US.UTF-8"  
ENV LANG "en_US.UTF-8"  
ENV LC_ALL "en_US.UTF-8"  
ENV LC_CTYPE "en_US.UTF-8"  
RUN mkdir -p /root/blogg  
RUN mkdir -p /root/.ssh  
RUN cd /root/blogg && git clone https://github.com/hackeriet/blog.git  
# RUN cd /root/blogg && git clone git://github.com/barryclark/jekyll-now.git  
RUN mv /root/blogg /srv/jekyll  
# RUN jekyll build  
#RUN cp -r /tmp/jekyll-site/_site/* /usr/share/nginx/html  
#RUN bundle exec jekyll serve  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Define environment variable  
ENV NAME World  
  
# Run app.py when the container launches  
# CMD ["python", "app.py"]  

