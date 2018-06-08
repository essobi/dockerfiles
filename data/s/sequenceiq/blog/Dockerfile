FROM ruby:1.9.3  
MAINTAINER lajos.papp@sequenceiq.com  
  
RUN apt-get update \  
&& apt-get install -y unzip  
  
RUN curl -Lo /usr/local/bin/jq
http://stedolan.github.io/jq/download/linux64/jq \  
&& chmod +x /usr/local/bin/jq  
  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
COPY server /usr/local/bin/server  
  
ENV SOURCE_REPO sequenceiq/blog-test  
ENV SOURCE_BRANCH source  
  
RUN git clone https://github.com/${SOURCE_REPO}.git /tmp/blog \  
&& cd /tmp/blog && git checkout ${SOURCE_BRANCH}  
  
ENV BLOG_DIR /tmp/blog  
WORKDIR /tmp/blog  
RUN bundle install  
  
COPY try-test-branch.sh /  
COPY github-release.sh /  
COPY deploy_live.sh /  
  
EXPOSE 8080  
ONBUILD COPY . /tmp/blog  
ONBUILD RUN rake generate  
  
CMD ["server", "-dir", "public/blog/", "-h", "0.0.0.0"]  

