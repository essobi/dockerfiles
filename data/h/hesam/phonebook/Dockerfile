# based on https://hub.docker.com/r/jacekmarchwicki/android/  
# Run following command inf this is your first time  
# $ docker build -t docker-phonebook ."  
# $ docker run --tty --interactive --volume=$(pwd):/opt/workspace
--workdir=/opt/workspace --rm docker-phonebook /bin/sh -c "./gradlew build"  
FROM jacekmarchwicki/android:latest  

