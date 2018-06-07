FROM trifork/mongooseim:1.5  
  
ADD https://github.com/esl/MongooseIM/archive/1.5.1.tar.gz
/tmp/mongooseim.tar.gz  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
erlang && \  
mkdir -p /src && \  
tar xzf /tmp/mongooseim.tar.gz --directory /src/ && \  
(cd /src/MongooseIM-1.5.1/ && ./rebar get-deps) && \  
rm -rf /var/lib/apt/lists/* /tmp/mongooseim.tar.gz  

