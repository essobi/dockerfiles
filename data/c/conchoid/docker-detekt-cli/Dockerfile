FROM gradle:4.6.0-jdk8-alpine AS detekt-cli  
  
RUN set -x \  
&& VERSION="RC6-4" \  
&& wget -q "https://github.com/arturbosch/detekt/archive/${VERSION}.tar.gz" \  
&& tar xzf "${VERSION}.tar.gz" \  
&& cd "detekt-${VERSION}/detekt-cli" \  
&& ( gradle shadowJar || for _ in $(seq 20); do sleep 5; gradle shadowJar &&
break; done ) \  
&& mkdir -p ~/detekt-cli \  
&& mv build/libs/*.jar ~/detekt-cli  
  
FROM scratch  
  
COPY \--from=detekt-cli /home/gradle/detekt-cli /detekt/detekt-cli  

