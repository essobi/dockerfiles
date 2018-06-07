###################################################  
# bleve-wiki-indexer Dockerfile  
# (see amazing http://www.blevesearch.com/)  
#  
# on Docker Hub  
# https://registry.hub.docker.com/u/lgsd/docker-bleve-wiki-indexer/  
#  
# on github:  
# https://github.com/lgs/docker-bleve-wiki-indexer  
#  
# VERSION 0.1  
#  
# bleve is a modern text indexing for Go  
# see online full text search engine:  
# http://wikisearch.blevesearch.com/search/  
#  
# Pull base image by google/golang  
# go version go1.3.1 linux/amd64  
# based on google/debian:wheezy:  
#  
# Linux version 3.11.0-18-generic (buildd@toyol)  
# gcc version 4.8.1 (Ubuntu/Linaro 4.8.1-10ubuntu8)  
# 32-Ubuntu SMP Tue Feb 18 21:11:14 UTC 2014  
###################################################  
  
FROM google/golang:stable  
  
MAINTAINER Luca G. Soave <luca.soave@gmail.com>  
  
# To force the upgrade of all the next packages  
# change REFRESHED_AT date, from time to time  
ENV REFRESHED_AT 2014-09-06  
  
RUN apt-get -qq update && \  
apt-get install -y cmake pkg-config && \  
go get -d github.com/libgit2/git2go && \  
cd $GOPATH/src/github.com/libgit2/git2go && \  
git submodule update --init && make install && \  
go get github.com/blevesearch/bleve-wiki-indexer && \  
mkdir /data && cd /data && \  
git clone https://github.com/blevesearch/bleve.wiki.git && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# EXPOSE 8099  
  
# WORKDIR $GOPATH/src/github.com/blevesearch/bleve-wiki-indexer  
# CMD ["/gopath/bin/bleve-wiki-indexer", "-dir", "/data/bleve.wiki"]  
  

