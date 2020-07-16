FROM python:latest
MAINTAINER Anta Stale
WORKDIR /home/anta/kurss/klie

COPY . .
CMD ["python", "tcpklients.py"]
