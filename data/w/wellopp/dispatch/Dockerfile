FROM ruby:2.4.1  
# essentials  
RUN apt-get update -qq  
RUN apt-get install -y build-essential software-properties-common apt-
transport-https  
  
# for postgres  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-
pgdg main"  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
# For gcloud  
RUN apt-add-repository "deb http://packages.cloud.google.com/apt cloud-sdk-
jessie main"  
RUN wget --quiet -O - https://packages.cloud.google.com/apt/doc/apt-key.gpg |
apt-key add -  
  
RUN apt-add-repository "deb [arch=amd64]
http://download.docker.com/linux/debian jessie stable"  
RUN wget --quiet -O - https://download.docker.com/linux/debian/gpg | apt-key
add -  
  
RUN apt-get update -qq  
RUN apt-get install -y postgresql-client-9.6 google-cloud-sdk kubectl docker-
ce  
  
# app  
ENV app /wellopp  
RUN mkdir $app  
WORKDIR $app  
  
# gems  
ADD Gemfile* $app/  
ENV BUNDLE_PATH $app/vendor/bundle  
ADD ./vendor/bundle $BUNDLE_PATH  
RUN bundle install --path $BUNDLE_PATH  
  
# files  
ADD . $app  
  
# I don't really understand why I sometimes need this. All the gems should be  
# downloaded and cached, but often gems with native extensions don't get  
# added correctly on the first go. Adding this second installation fixes it.  
# Is this real life?  
RUN bundle install --path $BUNDLE_PATH

