FROM sanjev/aws-cli-docker  
ENTRYPOINT aws ecr get-login | /bin/ash && docker tag $IMAGE $TARGET && docker
push $TARGET

