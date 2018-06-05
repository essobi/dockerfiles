# Run Rainbowstream in a container  
#  
# docker run -it --rm \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v $PWD:/home/boilr/cwd \  
# -v $HOME/.config/boilr:/home/boilr/.config/boilr \  
# --name boilr \  
# seagoj/docker-boilr  
FROM golang  
LABEL maintainer "Jeremy Seago <seagoj@gmail.com>"  
  
RUN groupadd -r boilr && useradd --no-log-init -r -g boilr boilr  
USER boilr  
WORKDIR /home/boilr/cwd  
RUN go get github.com/tmrts/boilr && go install github.com/tmrts/boilr  
  
ENTRYPOINT [ "boilr" ]  

