FROM ubuntu-debootstrap  
MAINTAINER Stefan Baur  
  
COPY overlay/ /  
  
RUN chmod +x /scripts/*; /scripts/setup; /scripts/cleanup -f bash sh dash cat
tail ps kill cp tty which mktemp rm mv mkdir ln chown grep groups ls du git
git-receive-pack git-shell git-upload-archive git-upload-pack sudo bundle node
nodejs npm grunt sharelatex.sh nc nc.traditional redis-benchmark redis-check-
aof redis-check-dump redis-cli redis-sentinel redis-server nc sleep mongo
mongodump mongofiles mongooplog mongorestore mongosniff mongotop mongod
mongoexport mongoimport mongoperf mongos mongostat env perl perl5.18.2 perlbug
perldoc perlivp perlthanks unzip zip gzip pngcrush aspell aspell-autobuildhash
aspell-import  
  
WORKDIR /data  
  
CMD /sharelatex.sh  
  
EXPOSE 3000  

