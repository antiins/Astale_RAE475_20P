# Astale_RAE475_20P
## PYTHON SOCKET klients

FROM python:3

RUN apt-get update
    apt-get install iputils-ping
    apt-get install python3

EXPOSE 5001

CMD echo "Sveiki no klienta programmas"

## PYTHON SORCKET serveris

FROM python:3

RUN apt-get update
    apt-get install iputils-ping
    apt-get python3
    
EXPOSE 5001

CMD echo "Hello from Server"

## PYTHON UDP serveris

FROM python:3

RUN apt-get update && apt-get install -y \
  python3 \
  nano \

EXPOSE 5005

CMD echo "Hello, World!"

## PYTHON UDP klients

FROM python:3

RUN apt-get update && apt-get install -y \
  python3 \
  nano \

EXPOSE 5005

CMD echo "Hello, World!"
