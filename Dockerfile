#Dockerfile #DockerImage #container 

FROM  python:3.8

WORKDIR /geohash_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./backend ./backend
WORKDIR /geohash_api/backend
CMD ["python", "geohash_api.py"]
 









