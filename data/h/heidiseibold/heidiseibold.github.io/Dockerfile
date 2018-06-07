# docker run --rm -p 8787:8787 -p 4000:4000 -v
/home/heidi/Documents/git/HeidiSeibold.github.io/:/home/rstudio blog  
# servr::jekyll(command = '/usr/local/bin/jekyll build')  
  
FROM rocker/hadleyverse  
## So that things like `top` and `less` work correctly  
ENV TERM xterm  
## Install basic ruby, javascript, and linux utils we need for the site ##  
RUN apt-get update \  
&& apt-get install -y -t unstable \  
bundler \  
nodejs \  
&& installGithub.r yihui/servr \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages  
  
COPY Gemfile /Gemfile  
RUN bundle update \  
&& bundle install  
  
## My git name, must be done for user pid 1000, and root  
RUN git config --global user.name 'HeidiSeibold' \  
&& git config --global user.email 'heidi.seibold@uzh.ch' \  
&& git config --global credential.helper 'cache --timeout=3600' \  
&& git config --global push.default simple  
  
### Expose port for jekyll serve ###  
EXPOSE 4000  

