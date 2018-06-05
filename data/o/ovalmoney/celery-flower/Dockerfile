FROM python:3.6.4-alpine3.6  
  
# Get latest root certificates  
RUN apk add --no-cache \  
ca-certificates \  
git \  
&& update-ca-certificates  
  
# Install the required packages  
RUN pip install \  
'redis==2.10.6' \  
'git+https://github.com/OvalMoney/flower.git@1.0'  
  
# PYTHONUNBUFFERED: Force stdin, stdout and stderr to be totally unbuffered.
(equivalent to `python -u`)  
# PYTHONHASHSEED: Enable hash randomization (equivalent to `python -R`)  
# PYTHONDONTWRITEBYTECODE: Do not write byte files to disk, since we maintain
it as readonly. (equivalent to `python -B`)  
ENV PYTHONUNBUFFERED=1 PYTHONHASHSEED=random PYTHONDONTWRITEBYTECODE=1  
  
# Default port  
EXPOSE 5555  
  
# Run as a non-root user by default, run as user with least privileges.  
USER nobody  
  
ENTRYPOINT ["flower"]

