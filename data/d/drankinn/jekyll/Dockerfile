FROM ubuntu:14.04  
MAINTAINER Lance Andersen <techlance@gmail.com>  
  
# Set locales  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Create editor userspace  
RUN groupadd jekyll  
RUN useradd jekyll -m -g jekyll -s /bin/bash  
RUN passwd -d -u jekyll  
RUN echo "jekyll ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jekyll  
RUN chmod 0440 /etc/sudoers.d/jekyll  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get install -y ruby ruby-dev git build-essential curl nodejs python-
pygments  
RUN apt-get clean && rm -rf /var/lib/apt/lists/  
  
# Install jekyll  
RUN gem install jekyll github-pages jekyll-redirect-from kramdown rdiscount
rouge  
  
# Change user, launch bash  
USER jekyll  
  
# Expose Code volume and jekyll port  
VOLUME "/home/jekyll"  
EXPOSE 4000  
WORKDIR /home/jekyll  
ENTRYPOINT ["jekyll"]  

