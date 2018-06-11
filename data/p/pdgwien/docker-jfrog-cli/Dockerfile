FROM ubuntu:18.04  
RUN apt-get update && apt-get install -y unzip curl zip grep  
RUN curl -XGET "https://api.bintray.com/content/jfrog/jfrog-cli-
go/\$latest/jfrog-cli-linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64" -L
-k > /usr/bin/jfrog && chmod u+x /usr/bin/jfrog

